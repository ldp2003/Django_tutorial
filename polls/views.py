from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question, Choice

def index(request):
    # context = {
    #     'title': 'My Polls App',
    #     'questions': ['Question 1', 'Question 2', 'Question 3'] giống kiểu dl bình thường nếu không có model truyền vào
    # }

    #thêm searching
    search_query = request.GET.get('search', '')  # mặc định là rỗng nếu không có -> giúp cái input search trong index nó tự nhiên hơn do ko có là mỗi lần vào text input nó hiện none
    if search_query:
        questions = Question.objects.filter(question_text__icontains=search_query)#.values()
        title = f"Search results for '{search_query}'"
    else:
        questions = Question.objects.all().values().order_by('-pub_date')
        title = 'My Polls App'

    context = {
        'title': title,
        'questions': questions,
        'search_query': search_query,
    }

    return render(request, 'polls/index.html', context) # render là shorcut, render dựa vào template

    # template = loader.get_template('polls/index.html') # cái này dài hơn nhưng chắc là có thể custom nhiều hơn ?
    # return HttpResponse(template.render(context, request))
    # request nên truyền vào nếu xài HttpResponse (render bắt phải truyền vào)

# def index(request):
#     template = loader.get_template('polls/index.html') 
#     return HttpResponse(template.render())

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist") đống string chưa biết dùng vào đâu ở 404 nma để sau coi lại
    # có thể shorcut đống check phía trên bằng get_object/list_or_404 (cần import)
    question = get_object_or_404(Question, id=question_id)

    choices = Choice.objects.filter(question=question) #.values()
    # choices = question.choice_set.all().values()  # Lấy tất cả các lựa chọn cho câu hỏi này
    # choices = get_list_or_404(Choice, question=question)
    # 3 cách trên đều được, cách dưới cùng auto raise 404 nếu không có
    # Mảng (queryset) có thẻ chuyển thành dict nhờ .values() nhưng cho dễ nhìn chứ template vẫn access bth
    # Đối với các query lấy về một object đơn lẻ thì không cần (?)

    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'polls/detail.html',  context)

def endpoint1(request):
    return HttpResponse("endpoint 1.")

def vote(request, question_id):
    if request.method == 'POST': 
        choice_id = request.POST.get('choice') #lấy từ value của form có name là 'choice'
        if choice_id:
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
    return HttpResponseRedirect(reverse('detail', args=(question_id,)))


def testing(request):
    template = loader.get_template('polls/testingTemplate.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))

#generic views
#chắc là dùng cho trang crud chỉ 1 model sẽ tiện và nhìn gọn hơn, phức tạp hoặc có nhiều model thì nên xài functional views như trên
from django.views.generic import ListView
class QuestionListView(ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'questions'
    paginate_by = 10