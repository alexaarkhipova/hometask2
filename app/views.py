from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ispum {i}'
        } for i in range(20)
    ]
def paginate(objects, page, per_page=20):
    paginator = Paginator(objects, per_page)
    return paginator.page(1)

def index(request):
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, 1)})

def onequestion(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'onequestion.html', { 'question': item })
def login(request):
    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')
def newquestion(request):
    return render(request, 'newquestion.html')
def settings(request):
    return render(request, 'settings.html')
def hotquestions(request):
    return render(request, 'hotquestions.html')
