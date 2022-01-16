from django.shortcuts import render

# Create your views here.
def sign_in(request):
	return render(request, 'sign-in.html')

def register(request):
	if request.method == "POST":
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		invi_code = request.POST.get('invi_code')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')