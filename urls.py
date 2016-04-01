from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
	# Accueil
	url(r'^$', views.index, name='index'),

	# Articles
	url(r'^articles/$', views.articles, name='articles'),
	url(r'^articles/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),

	# Fact & Curious
	url(r'^fact_and_curious/$', views.fact_and_curious, name='fact_and_curious'),
	url(r'^fact_and_curious/(?P<pk>[0-9]+)/$', views.fact_and_curious_detail, name='fact_and_curious_detail'),

	# Vu sur le Web
	url(r'^seen_on_the_web/$', views.seen_on_the_web, name='seen_on_the_web'),
	url(r'^seen_on_the_web/(?P<pk>[0-9]+)/$', views.seen_on_the_web_detail, name='seen_on_the_web_detail'),

	# L'Équipe
	url(r'^team/$', views.team, name='team'),

	# Mentions Légales
	url(r'^legal_notices/$', views.legal_notices, name='legal_notices'),

	# Ligne à supprimer au déploiement
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,})
]