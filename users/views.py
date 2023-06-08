from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from .utils import searchProfiles
from posts.models import Post

# Create your views here.

def home (request):
    return render (request, "landing.html")


def loginUser(request):
#this stops authenticated user from seeing the login page
    page = 'login'
    if request.user.is_authenticated:
        return redirect('timeline') 
    
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('timeline')
        else:
            messages.error(request, 'Username OR password is incorrect.')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'Logged out, goodbye!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account is created!')

            login(request, user)
            return redirect('timeline')
        
        else:
            messages.success(request, 'Error occurred during registration, try again.')

    context = {'page':page, 'form':form}
    return render(request, 'users/register.html', context)


#specific user profile
def profiles(request, pk):
    profiles = Profile.objects.get(id=pk)

    if request.user.is_authenticated:
        if request.method == "POST":
            current_user_profile=request.user.profile
            action = request.POST.get('action')
            
            if action == "unfollow":
                current_user_profile.follows.remove(profiles)
            elif action == "follow":
                current_user_profile.follows.add(profiles)
        request.user.profile.save()

    posts_with_images = profiles.post_set.exclude(image__exact='')
    posts_without_images = profiles.post_set.filter(image__exact='')

    context = {'profiles': profiles, 'posts_with_images': posts_with_images, 'posts_without_images': posts_without_images}
    return render(request, 'users/profiles.html', context)


#account of the logged in user
@login_required(login_url="login")
def useraccount(request):
    profile = request.user.profile
    posts_with_images = profile.post_set.exclude(image__exact='')
    posts_without_images = profile.post_set.filter(image__exact='')
    context = {'profile': profile, 'posts_with_images': posts_with_images, 'posts_without_images': posts_without_images}
    return render(request, 'users/account.html', context)


@login_required(login_url="login")
def editaccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)




def userlist(request):
    userprofiles, search_query = searchProfiles(request)
    # userprofiles = Profile.objects.all().order_by("created")
    return render(request, "users/userlist.html", {'userprofiles': userprofiles, 'search_query': search_query})


@login_required(login_url="login")
def addtofavorites(request, pk):
    posts = get_object_or_404(Post, id=pk)
    if posts.favorites.filter(id=request.user.id):
        posts.favorites.remove(request.user)
        messages.success(request, 'Removed from favorites.')
    else: 
        posts.favorites.add(request.user)
        messages.success(request, 'Added to favorites.')

    return HttpResponseRedirect(reverse('postdetails', args=[str(pk)]))


@login_required(login_url="login")
def favoritelist(request):
    favorite_posts = Post.objects.filter(favorites=request.user)
    return render(request, 'users/favorites.html', {'favorite_posts': favorite_posts})