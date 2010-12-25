from django.db import models
from django import forms

from champs.models import Titre

class TitleField(forms.CharField):

	def prepare_value(self, value):
		for t in Titre.objects.all():
			if t.id == value:
				return Titre.objects.get(pk=value)
		return ""