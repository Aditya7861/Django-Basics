import datetime
from django.utils import timezone
from django.db import models
class Questions(models.Model):

    def __str__(self):
        return self.question_text
    def was_published(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=240)
    pub_data = models.DateTimeField("date published")

class Choice(models.Model):

    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=280)
    votes = models.IntegerField(default=0)
