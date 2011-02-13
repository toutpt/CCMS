from django.conf.urls.defaults import *

urlpatterns = patterns('pages.views',
    (r'^$', 'index', { 'template_name':'pages/index.html'}, 'pages_home'),
	(r'^categorie/(?P<categorie_alias>[-\w]+)/$',
		'show_category', { 'template_name':'pages/categorie.html'},'pages_categorie'),
	(r'^ajouter_categorie/$',
		'ajouter_categorie', { 'template_name':'pages/categorie_add.html'},'pages_categorie_add'),
	(r'^article/(?P<article_alias>[-\w]+)/$',
		'show_article', {'template_name':'pages/article.html'},'pages_article'),
)
