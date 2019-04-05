from django.db import models
from django.core.validators import MaxValueValidator


class IdolDetail(models.Model):

	aboutme = models.TextField()
	birthday = models.DateField()
	city = models.CharField(max_length=20)
	height = models.PositiveIntegerField(validators=[MaxValueValidator(300)], help_text='Please input in CM')
	profilepicture = models.ImageField(upload_to='gallery', default='gallery/default.png', null=True, blank=True)
	namefirst = models.CharField(max_length=100)
	namelast = models.CharField(max_length=100)
	namemiddle = models.CharField(max_length=100, null=True, blank=True)
	nickname = models.CharField(max_length=15)
	province = models.CharField(max_length=20)
	school = models.CharField(max_length=50)
	votes = models.PositiveIntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return self.namefirst + " " + self.namelast
			