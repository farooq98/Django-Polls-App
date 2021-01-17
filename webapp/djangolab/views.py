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
        option_id = int(request.POST.get("radioBtn"))
        choice = Options.objects.get(id=option_id)
        choice.votes += 1
        choice.save()
        return render(request, "djangolab/thankyou.html")

def submitResponse(request):
    return render(request, "djangolab/thankyou.html")

def showResults(request):
    questions = Question.objects.all()
    return render(request, "djangolab/results.html", {"data":questions})
