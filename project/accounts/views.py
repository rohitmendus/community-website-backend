from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import Profile
import math
import random
import re

# Create your views here.
def sign_in(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = auth.authenticate(username=email, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect("/dashboard")
		else:
			messages.info(request, "Incorrect email or password!")
			return redirect("/sign-in")
	return render(request, 'sign-in.html')

def show_register(request, tab):
	return render(request, 'sign-in.html', {'tab':tab})


def number_generator():
	digits = [i for i in range(10)]
	random_num = ""
	for i in range(6):
		index = math.floor(random.random() * 10)
		random_num += str(digits[index])
	return int(random_num)

def register(request):
	if request.method == "POST":
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		invi_code = request.POST.get('invi_code')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		inputs = [f_name, l_name, invi_code, email, password1, password2]
		regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
		if '' not in inputs:
			if (re.fullmatch(regex, email)):
				if password1 == password2:
					if User.objects.filter(email=email).exists() == False:
						if Profile.objects.filter(invi_code=invi_code).exists():
							username = f_name + "_" + l_name
							username = username.lower()
							user = User.objects.create_user(username=username, email=email, password=password1, first_name=f_name, last_name=l_name)
							user.save()	
							new_invi_code = number_generator()
							user_profile = Profile(user=user, invi_code=new_invi_code)
							user_profile.save()
							auth.login(request, user)
							return redirect("/dashboard")
						else:
							messages.info(request, 'Invitation Code is not valid!')
							return redirect('/sign-in')
					else:
						messages.info(request, 'Same Email is already registered!')
						return redirect('/sign-in')
				else:
					messages.info(request, 'Passwords are not matching!')
					return redirect('/sign-in')
			else:
				messages.info(request, 'Email is not valid!')
				return redirect('/sign-in')
		else:
			messages.info(request, 'Some fields are empty!')
			return redirect('/sign-in')
	else:
		return redirect('/sign-in')
		
def logout(request):
	auth.logout(request)
	return redirect("/")