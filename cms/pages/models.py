# -*- coding: utf-8 -*- 

import datetime

from django.contrib.auth.models import User
from django.db import models


class Categorie(models.Model):
	#cat = models.ForeignKey("self", verbose_name="Catégorie parente")
	titre = models.CharField("Titre", max_length=200)
	alias = models.SlugField("Alias", max_length=200, unique=True)
	etat_choix = (
		(1, "Publié"),
		(2, "Non publié"),
		(3, "Archivé"),
	)
	etat = models.IntegerField("Etat", choices=etat_choix, default=1)
	description = models.TextField("Description", blank=True)
	
	class Meta:
		ordering = ['titre']
	
	def __unicode__(self):
		return self.titre
		
		

class Article(models.Model):
	titre = models.CharField("Titre", max_length=200)
	contenu = models.TextField("Contenu", blank=True)
	date_pub = models.DateTimeField("Date de publication", default=datetime.datetime.now)
	
	# Metadata
	alias = models.SlugField("Alias", max_length=200, unique=True)
	auteur = models.ForeignKey(User, verbose_name="Auteur")
	etat_choix = (
		(1, "Publié"),
		(2, "Non publié"),
		(3, "Archivé"),
	)
	etat = models.IntegerField("Etat", choices=etat_choix, default=1)
	
	# Catégorisation
	categories = models.ForeignKey(Categorie, verbose_name="Catégorie")
	
	class Meta:
		ordering = ['-date_pub']
	
	def __unicode__(self):
		return self.titre
