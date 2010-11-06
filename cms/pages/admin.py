from django.contrib import admin
from pages.models import Article
from pages.models import Categorie

class CategorieAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)


	
