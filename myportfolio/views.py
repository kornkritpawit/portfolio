from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from .models import ContactUs
# Create your views here.
from .forms import *

def index(request):
  # template = loader.get_template('myportfolio/index.html')
  # return HttpResponse(template.render())
  # return HttpResponse("Hello, world. You're at the portfolio index.")
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print("valid")
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            contact = ContactUs(email=from_email, subject=subject, message=message)            
            try:
              contact.save()
              print('successful')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    return render(request, "myportfolio/index.html", {'form': form})
