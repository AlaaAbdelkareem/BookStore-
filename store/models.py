from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=200)
	bio = models.TextField()
	pic = models.ImageField(upload_to = "static/images")
	DOB = models.DateTimeField()
	DOD = models.DateTimeField(null=True)
	country = (
        ('EG', 'Egypt'),
        ('USA', 'United States'),
        ('UK', 'United Kingdom'),
        ('UAE', 'United Arab'),
    )
	follow = models.ManyToManyField(User)
	def __str__(self):
		return self.name

class Category(models.Model):
	title = models.CharField(max_length=200)
	like = models.ManyToManyField(User)
	description = models.TextField()
	pic = models.ImageField(upload_to = "static/images")
	def __str__(self):
		return self.title

class Book(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(null=True)
	pic = models.ImageField(upload_to = "static/images")
	published_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey('Author',on_delete=models.CASCADE)
	cat_books = models.ManyToManyField(Category)
	# read = models.ManyToManyField(User,related_name='read', null=True)
	read = models.ManyToManyField(User,related_name='read', blank=True)
	wish =  models.ManyToManyField(User,related_name='wish', blank=True)
	# review = models.ManyToManyField(User,related_name='review')
	def __str__(self):
		return self.title

class Rate(models.Model):
	rate = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

