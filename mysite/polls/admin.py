from django.contrib import admin
from .models import Question

# Register your models here.

admin.site.register(Question)    # 在这里注册了以后在admin界面才可以看得见这个类


