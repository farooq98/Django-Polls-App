from django.shortcuts import render


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

def show(request):
    return render(request, 'djangolab/index.html', {"data":data})

def about(request):
    return render(request, 'djangolab/about.html')


