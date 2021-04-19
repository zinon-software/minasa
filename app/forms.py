from django import forms
from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ['question','answer_1','choice_1','answer_2','choice_2','answer_3','choice_3','grades',]

