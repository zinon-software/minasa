from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subject)
admin.site.register(Questions)
admin.site.register(Students)
admin.site.register(Solutions)