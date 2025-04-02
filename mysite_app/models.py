from django.db import models

# Create your models here.
# two models: Questions- text, pub_date : Choice- text, votes

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
class Choice(models.Model):
    # on_delete = models.cascade means that if record in parent table is deleted then all related records in child table automatically deleted. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0)  
