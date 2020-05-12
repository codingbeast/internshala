from django.shortcuts import render, HttpResponse

def login(request):
	return HttpResponse("hi")
def dashboard(request):
	return HttpResponse("nice")

def personal_details(request):
	return render(request,"accounts/home.html")