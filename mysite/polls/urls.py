from django.urls import path
from . import views

# 为了让django分辨重名的url,如果其它应用中也有detail.html,那么{% url %}标签该如何对应寻找呢
'''这里的views.IndexView.as_view()中的IndexView是方法名'''

app_name = 'polls'
'''
    改良视图URLconf
    通用视图而可以让我们不再需要写views.py，也可以渲染出html
'''
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]


'''普通视图URLconf'''
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),

# ]