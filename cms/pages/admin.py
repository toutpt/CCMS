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

	class Meta:
		model = Categorie

	def clean_titre(self):
		t = Titre(titre=self.cleaned_data['titre'])
		for e in Titre.objects.all():
			if t.titre == e.titre:
				return Titre.objects.get(titre=self.cleaned_data['titre'])
		t.save()
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


	
