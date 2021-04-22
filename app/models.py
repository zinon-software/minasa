from django.db import models
from django.contrib.auth.models import User

# Create your models here.
QUESTION_TYPE = (
    ('A', 'خيارات'),
    ('B', 'صح وخطأ'),
    ('C', 'وصل'),
)

class Subject(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, unique=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Questions(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='subject')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_created_by')
    question = models.CharField(max_length=255, null=True, blank=True)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE, default = 'A')
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
    name = models.CharField(max_length=50, null=True, blank=True, unique=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_student')
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Solutions(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE, related_name='questions')
    student_by = models.ForeignKey(Students,on_delete=models.CASCADE, related_name='students')
    solution = models.CharField(max_length=255, null=True, blank=True)