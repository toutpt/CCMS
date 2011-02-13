from pages.models import Categorie
from cms import settings

def cms(request):
	return {
		'active_categories': Categorie.objects.all(),
		#'site_name': settings.SITE_NAME,
		#'meta_keywords': settings.META_KEYWORDS,
		#'meta_description': settings.META_DESCRIPTION,
		'request': request
	}