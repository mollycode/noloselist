from django.db import models
from django.forms import ModelForm

TYPE_CHOICES = (
	('DO', 'Do This!'),
	('GET', 'Get This!'),
	('REM', 'Remember This!'),
)

class Item(models.Model):
	task = models.CharField(max_length=150)
	typs = models.CharField(max_length=3, choices=TYPE_CHOICES)
	due = models.DateField()
	alert = models.BooleanField()
	active = models.BooleanField(default = True)

	def __str__(self):
		return self.task

class ItemForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['task'].label = "Don't forget"
		self.fields['typs'].label = "Pick a list"
		self.fields['due'].label = "Do by"
		self.fields['alert'].label = "Remind me"
	
	class Meta:
		model = Item
		exclude = ('active',)