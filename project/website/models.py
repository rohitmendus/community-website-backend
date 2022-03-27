from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class friend_requests(models.Model):
	from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)


class Articles(models.Model):
	title = models.CharField(max_length=200, null=True)
	text = models.TextField(max_length=4000, null=True)
	author = models.ForeignKey(User, related_name="articles", blank=True, on_delete=models.CASCADE)
	date_posted = models.DateField(auto_now=True)

class ArticleLikes(models.Model):
	article = models.ForeignKey(Articles, related_name="likes", blank=True, on_delete=models.CASCADE)
	liked_by = models.ForeignKey(User, related_name="articles_liked", blank=True, on_delete=models.CASCADE)	

class ArticleComments(models.Model):
	article = models.ForeignKey(Articles, related_name="comments", blank=True, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500, null=True)
	posted_by = models.ForeignKey(User, related_name="articles_commented", blank=True, on_delete=models.CASCADE)
	date_posted = models.DateField(auto_now=True)

class BookReviews(models.Model):
	book_title = models.CharField(max_length=200, null=True)
	posted_by = models.ForeignKey(User, related_name="book_reviews", blank=True, on_delete=models.CASCADE)
	book_cover = models.ImageField(upload_to="pics", null=True)
	date_posted = models.DateField(auto_now=True)
	review = models.TextField(max_length=500, null=True)
	shop_url = models.URLField(null=True)
	rating = models.FloatField(default=0, 
		validators=[
			MinValueValidator(0.0), 
			MaxValueValidator(5.0)
		])

class GalleryImages(models.Model):
	image = models.ImageField(upload_to="pics", null=True)
	caption = models.CharField(max_length=200, null=True)
	posted_by = models.ForeignKey(User, related_name="images_posted", blank=True, on_delete=models.CASCADE)
	date_posted = models.DateField(auto_now=True)
	
class ImageLikes(models.Model):
	image = models.ForeignKey(GalleryImages, related_name="likes", blank=True, on_delete=models.CASCADE)
	liked_by = models.ForeignKey(User, related_name="images_liked", blank=True, on_delete=models.CASCADE)	
