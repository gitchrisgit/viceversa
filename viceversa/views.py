from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    print(user_text[::-1])
    return render(request, 'reverse.html', {'reversed_usertext': user_text[::-1]})
