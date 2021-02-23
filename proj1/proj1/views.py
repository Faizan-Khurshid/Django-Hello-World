from django.shortcuts import HttpResponse, render

def index(request):
  return render(request, 'home.html')

def contact(request):
  return HttpResponse("I am contact page")