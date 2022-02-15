from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class friend_requests(models.Model):
	from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)


class Articles(models.Model):
	title = models.CharField(max_length=100, null=True)
	text = models.TextField(max_length=500, null=True)
	author = models.ManyToManyField(User, related_name="articles", blank=True)
	date_posted = models.DateField(auto_now=True)
	like = models.IntegerField(null=True, default=0)

class ArticleComments:
	article = models.ManyToManyField(Articles, related_name="articles", blank=True)
	comment = models.TextField(max_length=500, null=True)
	like = models.IntegerField(null=True, default=0)
	posted_by = models.ManyToManyField(User, related_name="article_comments", blank=True)
	date_posted = models.DateField(auto_now=True)

class Books(models.Model):
	title = models.CharField(max_length=100, null=True)
	posted_by = models.ManyToManyField(User, related_name="books", blank=True)
	cover = models.ImageField(upload_to="pics", null=True)
	date_posted = models.DateField(auto_now=True)

class BookReview(models.Model):
	book = models.ManyToManyField(Books, related_name="book_reviews", blank=True)
	posted_by = models.ManyToManyField(User, related_name="book_review", blank=True)
	review = models.TextField(max_length=500, null=True)
	rating = models.FloatField(default=0, 
		validators=[
			MinValueValidator(0.0), 
			MaxValueValidator(5.0)
		])
	date_posted = models.DateField(auto_now=True)

class GalleryImages(models.Model):
	image = models.ImageField(upload_to="pics", null=True)
	caption = models.CharField(max_length=100, null=True)
	posted_by = models.ManyToManyField(User, related_name="galley_images", blank=True)
	like = models.ManyToManyField(User, related_name="images", blank=True)