from django.shortcuts import render
from .models import Question, Options

data = [
    {
        "id": 1,
        "date" : "11/12/2020",
        "question": "What is your name?",
    },
    {
        "id": 2,
        "date" : "01/01/2021",
        "question": "What is your firend name?",
    },
    {
        "id": 3,
        "date" : "28/08/2020",
        "question": "What is your favourite programming Language?",
    },
]

options = {
    1: [
        "Farooq",
        "Shahzaib",
        "Talha",
    ],
    2: [
        "Areeb",
        "Huzaifa",
        "Umer",
    ],
    3: [
        "Java",
        "Python",
        "C#",
    ]
}

def show(request):
    question = Question.objects.all()
    return render(request, 'djangolab/index.html', {"data":question})

def about(request):
    pass

def getData(request, **kwargs):
    question_id = kwargs["question_id"]
    question = Question.objects.get(pk=question_id)
    opt = question.options_set.all()
    print(opt)
    return render(request, 'djangolab/about.html', {"data": opt, "question": question})


