from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Questions(models.Model):
    QUESTION_TYPE = (
        ('A', 'خيارات'),
        ('B', 'صح وخطأ'),
        ('C', 'وصل'),
    )
    subject = models.ForeignKey(Subject,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    question = models.CharField(max_length=255, null=True, blank=True)
    # question_type = models.CharField(max_length=1, choices=QUESTION_TYPE)
    trueAndfalse = models.BooleanField(null=True, blank=True)
    answer_1 = models.CharField(max_length=255, null=True, blank=True)
    choice_1 = models.BooleanField(default=False, null=True, blank=True)
    answer_2 = models.CharField(max_length=255, null=True, blank=True)
    choice_2 = models.BooleanField(default=False, null=True, blank=True)
    answer_3 = models.CharField(max_length=255, null=True, blank=True)
    choice_3 = models.BooleanField(default=False, null=True, blank=True)
    grades = models.IntegerField()
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Students(models.Model):
    name = models.CharField(max_length=50,unique=True, null=True, blank=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Solutions(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    student_by = models.ForeignKey(Students,on_delete=models.CASCADE)
    solution = models.CharField(max_length=255, null=True, blank=True)