
from django.db import models
from django.utils import timezone



class Todo(models.Model):
  title = models.CharField(max_length=120, blank=False, default='')
  description = models.TextField(max_length=200,blank=False, default='')
  completed = models.BooleanField(default=False)
  data_publikacji = models.DateField(blank=True, default=timezone.now)
  
  def _str_(self):
    return self.title