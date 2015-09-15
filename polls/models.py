import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = (
	('d', 'Draft'),
	('p', 'Published'),
	('w', 'Withdrawn'),
)

class Question(models.Model):
	"""A model to hold the record for the questions.
	"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'	
	
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)	
	def __str__(self):
		return self.choice_text

