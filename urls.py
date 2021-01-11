from django.urls import path
from .import views


urlpatterns = [
	path('', views.index),
	path('aboutus/', views.aboutus),
	path('services/', views.services),
	#path('contact/', views.contact),
	path('bookdetails/', views.bookdetails),]
	#path('success/', views.success),
	#path('addbook/', views.addbook),
	

