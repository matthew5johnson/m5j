from django.shortcuts import render

# Create your views here.
def site_homepage(request):
	return render(request, 'writing/site_homepage.html')

def writing_home(request):
	return render(request, 'writing/writing_home.html')