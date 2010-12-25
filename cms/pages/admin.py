# -*- coding: utf-8 -*- 

from django.contrib import admin
from django.db import models
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
		self.initTitre = kwargs['instance'].titre
		
	
	def clean_titre(self):
		#print("Old Value :")
		#print(self.initTitre)
		oldTitre = Titre(titre=self.initTitre)
		newTitre = Titre(titre=self.cleaned_data['titre'])
		for e in Titre.objects.all():
			if e.titre == newTitre.titre:
				return Titre.objects.get(titre=self.cleaned_data['titre'])
		if newTitre.titre == self.initTitre:
			print("It's the same value")
		else:
			for k in Titre.objects.all():
				if k.titre == oldTitre.titre:
					k.titre == newTitre.titre
			print("Titre updated")
		newTitre.save()
		return Titre.objects.get(titre=self.cleaned_data['titre'])
	
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


class CategorieAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	form = CategorieForm
	
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	form = ArticleForm

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)


	
