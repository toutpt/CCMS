# -*- coding: utf-8 -*- 

from django.db import models

class Titre(models.Model):
	titre = models.CharField("Titre", max_length=200, unique=True)
	#instances = models.PositiveIntegerField("Instances")
	
	def __unicode__(self):
		return self.titre
