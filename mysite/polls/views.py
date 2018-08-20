from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render   
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

'''
    1.返回一个包含请求页面内容的HttpResponse对象
    2.抛出一个异常
'''
# Create your views here.


# '''展示数据库里以发布日期排序的最近5个投票问题'''
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]    # 找到最新发布的前五个问题
#     template = loader.get_template('polls/index.html')                   # 给出要渲染的页面
#     context = {'latest_question_list': latest_question_list,}            # 转为上下文
#     # return HttpResponse(template.render(context,request))                # 给出response，给出响应
#     '''这里给出的是另一个常用的做法'''
#     return render(request, 'polls/index.html', context)      # 使用这个方法的话就不用导入loader和HttpResponse了


# '''
#     为了不增加模型层和视图层的耦合性
#     所以尽量使用get_object_or_404()而不是自己捕获错误
#     抛出的是Http404而不是ObjectDoesNotExist

#     还有get_list_or_404()，当列表为空的时候抛出异常
# '''
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # try:
#     #     question = Question.objects.get(pk=question_id)    # 如果对应的question对象找不到的话就报404错误
#     # except Question.DoesNotExist:    # x效果就是会返回一个错误页面
#     #     print('catch exception')
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html',{'question':question})     # 传给视图函数   


# def results(request, question_id):
#     response = "You are looking at the results of question %s."
#     return HttpResponse(response % question_id)



# '''
#     request.POST[]是一个类字典对象
#     让你可以通过关键字的名字获取提交的数据
#     request.POST[]的返回值永远是一个字符串
#     如果request.POST['choice']数据中没有提供choice，POST将引发一个KeyError
# '''
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)    # 如果没有对应question_id的question对象，就会404not found
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html',{
#             'question': question,
#             'error_message': "You didn't select a choice",
#         })
#     else:
#         selected_choice.votes += 1     # 更新数据库里的信息
#         selected_choice.save()
#     '''HttpResponseRedirect()只接受一个参数，用户将要被重定向的url'''
#     '''
#         reverse()这个函数避免了我们在视图函数中硬编码url
#         @param1:我们想要跳转的视图的名字
#         @param2:该试图所对应的url模式中需要给该视图所提供的参数
#     '''
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#     def results(request, question_id):
#         question  = get_object_or_404(Question, pk=question_id)
#         return render(request, 'polls/results.html',{'question': question})


    
'''
    普通视图：
    1.根据URL中的参数从数据库中取出数据
    2.载入模板文件然后返回选然后的模板

    通用视图:
    1.转换URLconf
    2.删除一些旧的，不再需要的视图
    3.基于Django的通用视图引入新的视图
'''


'''
    ListView：显示一个对象列表
    DetailView：显示一个特定类型对象的详细信息页
    每个通用视图都需要知道自己对应的是哪种模型，这由model属性提供
    DetailView期望从URL中捕获名为pk的主键值，所以我们为通用视图把question_id改为pk
    
    默认情况下：
    通用视图DetailView使用<app name>/<model name>_detail.html的模板
    在我们的例子中，它将使用polls/question_detail.html模板

    视图ListView使用<app name>/<model name>_list.html的默认模板
    使用template_name告诉ListView使用我们创建的已经存在的"polls/index.html"模板
    而不是去用它自动生成的默认的名字

    对于DetailView，question变量会自动提供，因为我们指定了使用的模型model:Question
    Django能够为context变量决定一个合适的名字，然而对于ListView，自动生成context变量是question_list
    为了覆盖这个行为，我们提供xintext_object_name属性，表示我们想用lastest_question_list
    
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five published questions'''
        return Question.objects.order_by('-pub_date')[:5]

# 确保detail视图和results视图在渲染时具有不同的外观，即使它们在后台都是同一个DetailView
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'




'''
    request.POST[]是一个类字典对象
    让你可以通过关键字的名字获取提交的数据
    request.POST[]的返回值永远是一个字符串
    如果request.POST['choice']数据中没有提供choice，POST将引发一个KeyError
'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)    # 如果没有对应question_id的question对象，就会404not found
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1     # 更新数据库里的信息
        selected_choice.save()
    '''HttpResponseRedirect()只接受一个参数，用户将要被重定向的url'''
    '''
        reverse()这个函数避免了我们在视图函数中硬编码url
        @param1:我们想要跳转的视图的名字
        @param2:该试图所对应的url模式中需要给该视图所提供的参数
    '''
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
