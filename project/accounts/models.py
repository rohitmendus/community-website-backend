from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	invi_code = models.IntegerField()
	bio = models.CharField(max_length=500, null=True)
	profile_pic = models.ImageField(upload_to="pics", null=True)
	twitter = models.URLField(null=True)
	facebook = models.URLField(null=True)
	instagram = models.URLField(null=True)
	linkedin = models.URLField(null=True)

	def __str__(self):
		return self.user.username