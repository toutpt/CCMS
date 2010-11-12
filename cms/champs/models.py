# -*- coding: utf-8 -*- 

from django.db import models

class Titre(models.Model):
	titre = models.CharField("Titre", primary_key=True, max_length=200)
	
	def __unicode__(self):
		return self.titre