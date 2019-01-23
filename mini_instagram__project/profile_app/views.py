from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from profile_app.models import Profile, Post
from datetime import datetime
from profile_app.forms import SignupForm, LoginForm, ProfileForm, UserForm, PostForm


def signup(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            password=password,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email')
        )

        user = authenticate(request, username=username, password=password)

        if 'picture' in request.FILES:
            picture = request.FILES['picture']

        Profile.objects.get_or_create(
            user=user,
            picture=picture
        )

        if user is not None:
            login(request, user)
        return redirect('/profile_app/newsfeed/')

    return render(request, 'signup.html', context={
        'signup_form': SignupForm(),
        'profile_form': ProfileForm(),
    })


def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        return redirect('/profile_app/newsfeed/')

    return render(request, 'login.html', context={'login_form': LoginForm()})


def logout_auth(request):
    logout(request)
    return redirect('/profile_app/login/')


def profile(request, profile_id):

    profile = Profile.objects.get(id=profile_id)
    followers = profile.follows.all()

    if request.method == 'POST':
        if 'picture' in request.FILES:
            picture = request.FILES['picture']

    return render(request, 'profile.html', context={
        'post_form': PostForm(),
        'profile': profile,
        'followers': followers,
    })

def list_users(request):
    if request.user.is_authenticated:
        user = request.user
        list_users = Profile.objects.all()


        return render(request, 'list_users.html', {'logged_in': True, 'list_users': list_users})
    else:
        return render(request, 'list_users.html', {'logged_in': False})


def newsfeed(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    post = Post.objects.all()

    if request.method == 'POST':
        if 'picture' in request.FILES:
            picture = request.FILES['picture']

            Post.objects.get_or_create(
                profile=profile,
                description=request.POST.get('description'),
                date=date,
                picture=picture
            )

    return render(request, 'newsfeed.html', context={
        'profile': profile,
        'post': post,
        })
