from django.shortcuts import render

# Create your views here.
def sign_in(request):
	return render(request, 'sign-in.html')