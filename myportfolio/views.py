from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
  template = loader.get_template('myportfolio/index.html')
  return HttpResponse(template.render())
  # return HttpResponse("Hello, world. You're at the portfolio index.")