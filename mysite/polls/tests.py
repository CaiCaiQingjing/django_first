import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

'''
    Django应用的测试应该写在应用的tests.py文件里
    测试系统会自动的在所有以tests开头的文件里寻找并且执行测试代码
'''
# Create your tests here.

'''
    cmd中使用python manage.py test polls进行测试
    python manage.py test polls 将会寻找polls应用里的测试代码
    
    
'''

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)     # 创建了一个未来提出的问题实例
        self.assertIs(future_question.was_published_recently(), False)    # 检查其返回值，应该是False