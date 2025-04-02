import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# two models: Questions- text, pub_date : Choice- text, votes

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("datee published")
    
    def __str__(self):
        return self.question_text+"test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    # on_delete = models.cascade means that if record in parent table is deleted then all related records in child table automatically deleted. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.question.question_text
