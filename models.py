from django.db import models
from datetime import datetime

class Article(models.Model):
	authors = models.ManyToManyField('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateField(default=datetime.now)
	image = models.ImageField(upload_to='mag/images/articles/')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['id']

class FactAndCurious(models.Model):
	authors = models.ManyToManyField('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateField(default=datetime.now)
	image = models.ImageField(upload_to='mag/images/fact_and_curious/')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['id']
		verbose_name = "Fact and Curious"
		verbose_name_plural = "Fact and Curious"

class SeenOnTheWeb(models.Model):
	authors = models.ManyToManyField('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateField(default=datetime.now)
	image = models.ImageField(upload_to='mag/images/seen_on_the_web/')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['id']
		verbose_name = "Seen on the Web"
		verbose_name_plural = "Seen on the Web"

class SocialNetworkLink(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()
	logo = models.ImageField(upload_to='mag/images/social_network/')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name = "Réseau social"
		verbose_name_plural = "Réseaux sociaux"