from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from accounts.models import Profile
from .models import friend_requests
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.validators import URLValidator
from django.contrib.auth.hashers import check_password
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
	context = {'pro_pic': pro_pic, 'pic': profile.profile_pic, 'invi_code': profile.invi_code}
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

	friendRequests = friend_requests.objects.filter(to_user=request.user)
	if friendRequests.exists():
		context["any_friend_requests"] = True
		frnd_requests = []
		for i in friendRequests:
			user = User.objects.get(id=i.from_user_id)
			first_name = user.first_name
			last_name = user.last_name
			profile_pic = Profile.objects.get(user_id=i.from_user_id).profile_pic
			frnd_pro_pic = True
			if profile_pic == "":
				frnd_pro_pic = False
			frnd_request = {"first_name": first_name, "last_name": last_name, 
			"profile_pic": profile_pic, "frnd_pro_pic": frnd_pro_pic}
			frnd_request["id"] = i.id
			frnd_requests.append(frnd_request)
		context["friend_requests"] = frnd_requests
	else:
		context["any_friend_requests"] = False

	friends = []
	for i in request.user.friends.all():
		user = User.objects.get(id=i.user_id)
		friend = {"first_name": user.first_name, "last_name": user.last_name, 
		"profile_pic": i.profile_pic, "id": user.id}
		friends.append(friend)
	context["friends"] = friends
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
	if request.method == "POST":
		pwd = request.user.password
		pwd1 = request.POST.get("pwd")
		check = check_password(pwd1, pwd)
		if check:
			user = User.objects.get(id=request.user.id)
			auth.logout(request)
			user.delete()
			return redirect("/")
		else:
			messages.info(request, "Password is incorrect!")
	return render(request, 'delete_account.html')


@login_required(login_url="/sign-in")
def add_friend(request, id):
	to_user = User.objects.get(id=id)
	from_user = request.user
	if to_user == from_user:
		return redirect("/dashboard")
	if from_user.friends.filter(user_id=id):
		name = to_user.first_name + " " + to_user.last_name
		messages.info(request, 'You are already friends with ' + name)
		return redirect("/dashboard")
	else:
		friend_request, created = friend_requests.objects.get_or_create(from_user=from_user, to_user=to_user)
		if created:
			to_user_name = to_user.first_name + " " + to_user.last_name
			messages.info(request, 'Friend request has been sent to '+to_user_name+'!')
			return redirect("/dashboard")
		else:
			messages.info(request, 'A request had already been sent, please wait!')
			return redirect("/dashboard")

@login_required(login_url="/sign-in")
def profile(request, id):
	if id==request.user.id:
		return redirect("/dashboard")
	user = User.objects.get(id=id)
	user_profile = Profile.objects.get(user_id=id)
	pro_pic=True
	if user_profile.profile_pic == "":
		pro_pic = False
	friends = []
	for i in user.friends.all():
		friend_user = User.objects.get(id=i.user_id)
		friend = {"first_name": friend_user.first_name, 
		"last_name": friend_user.last_name, 
		"profile_pic": i.profile_pic, "id": friend_user.id}
		friends.append(friend)
	context = {'profile': {'first_name': user.first_name, 'last_name': user.last_name, 
	'email': user.email, 'bio': user_profile.bio, 'profile_pic': user_profile.profile_pic, 
	'twitter': user_profile.twitter, 'facebook': user_profile.facebook, 
	'instagram': user_profile.instagram, 'linkedin': user_profile.linkedin, 
	'pro_pic': pro_pic, "id": user.id, 'friends': friends}}
	return render(request, "profile.html", context)


def accept_friend_request(request, id):
	friend_request = friend_requests.objects.get(id=id)
	if friend_request.to_user == request.user:
		new_friend = friend_request.from_user.first_name + " " + friend_request.from_user.last_name
		user1 = Profile.objects.get(user=friend_request.to_user)
		user2 = Profile.objects.get(user=friend_request.from_user)
		user1.friends.add(friend_request.from_user)
		user2.friends.add(friend_request.to_user)
		friend_request.delete()
		messages.info(request, new_friend + " has been added to your friends' list!")
		return redirect("/dashboard")
	return redirect("/dashboard")

def decline_friend_request(request, id):
	friend_request = friend_requests.objects.get(id=id)
	if friend_request.to_user == request.user:
		friend_request.delete()
		return redirect("/dashboard")
	return redirect("/dashboard")

@login_required(login_url="/sign-in")
def change_password(request):
	if request.method == "POST":
		pwd = request.user.password
		pwd1 = request.POST.get("pwd1")
		check = check_password(pwd1, pwd)
		if check:
			pwd2 = request.POST.get("pwd2")
			pwd3 = request.POST.get("pwd3")
			if pwd2==pwd3:
				request.user.set_password(pwd2)
				request.user.save()
				update_session_auth_hash(request, request.user)
				return redirect("/dashboard")
			else:
				messages.info(request, "Passwords are not matching!")
		else:
			messages.info(request, "Password is incorrect!")
	return render(request, 'change_password.html')