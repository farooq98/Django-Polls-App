from django.shortcuts import render
from .models import Question, Options

def show(request):
    question = Question.objects.all()
    return render(request, 'djangolab/index.html', {"data":question})

def about(request):
    pass

def getData(request, **kwargs):
    if request.method == "GET":
        question_id = kwargs["question_id"]
        question = Question.objects.get(pk=question_id)
        opt = question.options_set.all()
        return render(request, 'djangolab/options.html', {"data": opt, "question": question})
    
    if request.method == "POST":
        print(request.POST)  
        return render(request, "djangolab/thankyou.html")


def submitResponse(request):
    return render(request, "djangolab/thankyou.html")


