from django.contrib import admin
from pages.models import Article
from pages.models import Categorie
from champs.models import Titre

class CategorieAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	raw_id_fields = ["titre"]
	
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	raw_id_fields = ['titre']


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)


	
