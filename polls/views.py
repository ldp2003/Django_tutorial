from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import Question, Choice

def index(request):
    # context = {
    #     'title': 'My Polls App',
    #     'questions': ['Question 1', 'Question 2', 'Question 3']
    # }
    questions = Question.objects.all().values()
    template = loader.get_template('polls/index.html')
    context = {
        'title': 'My Polls App',
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

# def index(request):
#     template = loader.get_template('polls/index.html') 
#     return HttpResponse(template.render())

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question).values()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'polls/detail.html',  context)

def endpoint1(request):
    return HttpResponse("Đây là kết quả của endpoint 1.")

def vote(request, question_id):
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
    return HttpResponseRedirect(reverse('detail', args=(question_id,)))
