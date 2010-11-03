from django.db import models

# Creation du modele du CMS

class Article(models.Model):
	titre = models.CharField('titre', max_length=200)				# Titre de l'article
	contenu = models.TextField('contenu', blank=True)				# Contenu de l'article
	date_pub = models.DateTimeField('date de publication')			# Date de publication de l'article
	traduit = models.BooleanField(default=False, editable=False)	# Article traduit
	
	def __unicode__(self):
		return self.titre
