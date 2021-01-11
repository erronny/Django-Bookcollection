from django.db import models

# Create your models here.

class Books(models.Model):
	title = models.CharField(max_length=80)
	author = models.CharField(max_length=100)
	isbn = models.CharField(max_length=30, unique=True)
	url = models.URLField()
	publisher = models.CharField(max_length=100)
	
	def __str__(self):
		return self.title+', '+self.author+', '+self.isbn+', '+self.url+', '+self.publisher
