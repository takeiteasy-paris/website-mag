from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

# Accueil
def index(request):
	article_list = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mag/index.html', {'article_list': article_list})

# Tous les articles
def articles(request):
	article_list = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mag/articles.html', {'article_list': article_list})

# Un seul article
def article_detail(request, pk):
	article = get_object_or_404(Article, pk=pk)
	return render(request, 'mag/article_detail.html', {'article': article})

# Tous les Fact & Curious
def fact_and_curious(request):
	fact_list = FactAndCurious.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mag/fact_and_curious.html', {'fact_list': fact_list})

# Un seul Fact & Curious
def fact_and_curious_detail(request, pk):
	fact = get_object_or_404(FactAndCurious, pk=pk)
	return render(request, 'mag/fact_and_curious_detail.html', {'fact': fact})

# Tous les Vu sur le Web
def seen_on_the_web(request):
	seen_list = SeenOnTheWeb.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mag/seen_on_the_web.html', {'seen_list': seen_list})

# Un seul Vu sur le Web
def seen_on_the_web_detail(request, pk):
	seen = get_object_or_404(SeenOnTheWeb, pk=pk)
	return render(request, 'mag/seen_on_the_web_detail.html', {'seen': seen})

# L'Équipe
def team(request):
	return render(request, 'mag/base.html', {'toto': "toto"})

# Mentions Légales
def legal_notices(request):
	return render(request, 'mag/legal_notices.html', {})