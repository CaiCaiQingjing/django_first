"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

'''这是URLconf文件'''
# include()理念：即插即用。投票应用有它自己的URLconf（polls/urls.py），在任何地方都应该能用
'''
    1.browser 输入/polls/34/
    2.django会载入mysite.urls模块
    3.找到匹配项'polls/'，切掉了匹配文本'polls/'，剩下'34/'发送至polls.urls'URLconf'做进一步处理
    4.在这里剩余文本匹配到了'<int:question_id>/' 使得django得以找到detail()进行调用
    5.detail(request=<HttpRequest object>,question_id=34)
'''

urlpatterns = [
    path('polls/', include('polls.urls')),      # 允许引用其它的urlconfs
    path('admin/', admin.site.urls),
]
