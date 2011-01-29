# -*- coding: utf-8 -*- 

from django.contrib import admin
from django.db import models
from django import forms

from pages.models import Article
from pages.models import Categorie
from champs.models import Titre
from fields.models import TitleField

from pages.forms import CategorieForm
from pages.forms import ArticleForm


class CategorieAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	form = CategorieForm
	
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	form = ArticleForm

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)


	
