from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

# from my Home app 
from .models import Books
#from .forms import ContactForm,Form,BooksForm


# Create your views here.


def index (request):
	return HttpResponse("<h1> Hello Welcome to index page </h1>")
		

def aboutus(request):
	return HttpResponse("<h1> Hello Welcome to About us page </h1>")

def services(request):
	return HttpResponse("<h1> Hello Welcome to services us page </h1>")

#def contact (request):
#	return render(request,'Home/contact.html',{})
	

def bookdetails(request):
	bookset = Books.objects.all()
	return render(request,'home/bookdetails.html',{'books' : bookset})
