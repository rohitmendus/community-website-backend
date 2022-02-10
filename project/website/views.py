from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .models import friend_requests
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import URLValidator
import re

# Create your views here.
def index(request):
	try:
		profile = Profile.objects.get(user=request.user)
		pro_pic = True
		if profile.profile_pic == "":
			pro_pic = False
		return render(request, 'index.html', {'pro_pic': pro_pic, 'pic': profile.profile_pic})
	except:
		pro_pic = False
		return render(request, 'index.html', {'pro_pic': pro_pic})

@login_required(login_url="/sign-in")
def dashboard(request):
	profile = Profile.objects.get(user=request.user)
	pro_pic = True
	if profile.profile_pic == "":
		pro_pic = False
	context = {'pro_pic': pro_pic, 'pic': profile.profile_pic}
	bio = profile.bio
	twitter = profile.twitter
	facebook = profile.facebook
	instagram = profile.instagram
	linkedin = profile.linkedin
	sm = ['bio', 'twitter', 'facebook', 'instagram', 'linkedin']
	social_media = [bio, twitter, facebook, instagram, linkedin]
	for x, i in enumerate(social_media):
		if i==None:
			context[sm[x]] = ''
		else:
			context[sm[x]] = i
	users = User.objects.filter(is_superuser=False)
	profiles = Profile.objects.all()
	context['users'] = users
	context['profiles'] = profiles
	return render(request, 'dashboard.html', context)


def change_info(request, id):
	if request.method == "POST":
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		email = request.POST.get('email')
		bio = request.POST.get('bio')
		file = request.FILES.get('profile-pic')
		inputs = [f_name, l_name, email, file]
		if '' not in inputs:
			regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
			if (re.fullmatch(regex, email)):
				if User.objects.filter(email=email).exists() == False or User.objects.get(id=id).email == email:
					user = User.objects.get(id=id)
					user.first_name = f_name
					user.last_name = l_name
					user.email = email
					user.save()
					profile = Profile.objects.get(user_id=id)
					profile.bio = bio
					if file != None:
						profile.profile_pic = file
					profile.save()
					return redirect("/dashboard")
				else:
					messages.info(request, 'Same Email is already registered!')
					return redirect("/dashboard")
			else:
				messages.info(request, 'Email is not valid!')
				return redirect("/dashboard")
		else:
			messages.info(request, 'Some fields are empty!')
			return redirect("/dashboard")
	else:
		return redirect("/dashboard")


def change_urls(request, id):
	if request.method == "POST":
		twitter = request.POST.get('twitter')
		facebook = request.POST.get('facebook')
		instagram = request.POST.get('instagram')
		linkedin = request.POST.get('linkedin')
		inputs = [twitter, facebook, instagram, linkedin]
		validate = URLValidator()
		for i in inputs:
			if len(i) != 0:
				try:
					validate(i)
				except:
					messages.info(request, 'Url is not valid!')
					return redirect("/dashboard")
		profile = Profile.objects.get(user_id=id)
		profile.twitter = twitter
		profile.facebook = facebook
		profile.instagram = instagram 
		profile.linkedin = linkedin
		profile.save()
		return redirect("/dashboard")
	return redirect("/dashboard")


@login_required(login_url="/sign-in")
def delete_account(request):
	return render(request, 'delete_account.html')


@login_required(login_url="/sign-in")
def add_friend(request, id):
	to_user = User.objects.get(id=id)
	from_user = request.user
	friend_request, created = friend_requests.objects.get_or_create(from_user=from_user, to_user=to_user)
	if created:
		to_user_name = to_user.first_name + " " + to_user.last_name
		messages.info(request, 'Friend request has been sent to '+to_user_name+'!')
		return redirect("/dashboard")
	else:
		messages.info(request, 'A request had already been sent, please wait!')
		return redirect("/dashboard")