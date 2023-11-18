from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ispum {i}'
        } for i in range(1, 101)
    ]
ANSWERS = [
        {
            'id': i,
            'title': f'Answer {i}',
        } for i in range(1, 101)
    ]
def paginate(objects, request, per_page):
    paginator = Paginator(objects, per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.page(1)
    return page_obj

def index(request):
    question_objects = QUESTIONS
    questions_page_obj = paginate(question_objects, request, per_page=20)
    context = {
        'objects': questions_page_obj,
        'questions': questions_page_obj,
    }
    return render(request, 'index.html', context)

def onequestion(request, question_id):
    answer_objects = ANSWERS
    item = QUESTIONS[question_id - 1]
    answers_page_obj = paginate(answer_objects, request, per_page=30)
    context = {
        'objects': answers_page_obj,
        'answers': answers_page_obj,
        'question': item,
    }
    return render(request, 'onequestion.html', context)
def login(request):
    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')
def taglist(request):
    return render(request, 'taglist.html')
def newquestion(request):
    return render(request, 'newquestion.html')
def settings(request):
    return render(request, 'settings.html')
def hotquestions(request):
    question_objects = QUESTIONS
    questions_page_obj = paginate(question_objects, request, per_page=20)
    context = {
        'objects': questions_page_obj,
        'questions': questions_page_obj,
    }
    return render(request, 'hotquestions.html', context)
