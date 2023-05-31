from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def monday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 3\n', 'exicise 4\n']
    return HttpResponse(todo_list)

def tuesday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 5\n']
    return HttpResponse(todo_list)

def wednesday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 5\n']
    return HttpResponse(todo_list)

def thursday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 5\n']
    return HttpResponse(todo_list)

def friday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 5\n']
    return HttpResponse(todo_list)

def saturday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 5\n']
    return HttpResponse(todo_list)

def sunday(request):
    todo_list = ['exicise 1\n', 'exicise 2\n', 'exicise 5\n', 'exicise 123\n']
    return HttpResponse(todo_list)