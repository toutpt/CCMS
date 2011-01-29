# -*- coding: utf-8 -*- 

from django import forms

from pages.models import Article
from pages.models import Categorie
from champs.models import Titre
from fields.models import TitleField


class CategorieForm(forms.ModelForm):
	
	titre = TitleField(label = "Titre")
	initTitre = ""

	class Meta:
		model = Categorie

	def __init__(self, *args, **kwargs):
		forms.ModelForm.__init__(self, *args, **kwargs)
		
		# Dans le cas d'une modification, on récupère le titre actuel
		if kwargs.get('instance'):
			self.initTitre = kwargs['instance']
	
	def update_one(self):
		
		# On crée un titre avec la nouvelle valeur du champ
		new = Titre(titre=self.cleaned_data['titre'])
		
		# On cherche si le nouveau titre existe déjà
		for old in Titre.objects.all():
			if old.titre == new.titre:
				return old
		
		# S'il n'existe pas, on sauvegarde le nouveau titre
		new.save()
		return Titre.objects.get(titre=self.cleaned_data['titre'])
	
	def update_all(self):
		
		# On crée un titre avec la nouvelle valeur du champ
		new = Titre(titre=self.cleaned_data['titre'])
		
		# On vérifie si un titre similaire existe
		for old in Titre.objects.all():
			if old.titre == new.titre:
				for oldCat in Categorie.objects.all():
					if self.initTitre:
						print(self.initTitre.titre.titre)
						if oldCat.titre.titre == self.initTitre.titre.titre:
							oldCat.titre = Titre.objects.get(titre=self.cleaned_data['titre'])
							oldCat.save()
				return old
		
		# Si non et si on modifie, on sauvegarde le titre et on refait l'opération
		if self.initTitre:
			new.save()
			for old in Titre.objects.all():
				if old.titre == new.titre:
					for oldCat in Categorie.objects.all():
						if oldCat.titre.titre == self.initTitre.titre.titre:
							oldCat.titre = Titre.objects.get(titre=self.cleaned_data['titre'])
							oldCat.save()
					return old
		
		# Si on crée un nouvel élément et le titre n'existe pas, on le sauvegarde
		new.save()
		return Titre.objects.get(titre=self.cleaned_data['titre'])
		
	def clean_titre(self):
		# return self.update_one()
		return self.update_all()
		
class ArticleForm(forms.ModelForm):
	
	titre = TitleField(label = "Titre")

	class Meta:
		model = Article

	def clean_titre(self):
		t = Titre(titre=self.cleaned_data['titre'])
		for e in Titre.objects.all():
			if t.titre == e.titre:
				return Titre.objects.get(titre=self.cleaned_data['titre'])
		t.save()
		return Titre.objects.get(titre=self.cleaned_data['titre'])