from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
	(r'^', include('pages.urls')),
	(r'^categories/$', 'pages.views.show_categories'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root' : '/Users/bnabilos/CCMS/cms/media' }),
	(r'^styles/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root' : '/Users/bnabilos/CCMS/cms/templates/styles' }),
	(r'^images/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root' : '/Users/bnabilos/CCMS/cms/images' }),
	
)
