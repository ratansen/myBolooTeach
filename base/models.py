from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    classs = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    paper_file = models.FileField(upload_to ='uploads/')
    answer_key = models.CharField(max_length=200,default="")
    marks_per_question = models.IntegerField(default=4)


    def __str__(self):
        return self.title