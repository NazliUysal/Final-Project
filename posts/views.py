from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from .models import Post, Like
from .forms import PostForm, CommentForm


@login_required(login_url="login")
def timeline(request):
    user = request.user.profile
    logged_in_user=request.user
    posts = Post.objects.filter(owner__followed_by__in=[user.id]).order_by("-posted")
    return render(request, "posts/timeline.html", {'user': user, 'posts': posts})

@login_required(login_url="login")
def post_details(request, pk):
    profile=request.user.profile
    postdetail = Post.objects.get(id=pk)

    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.post = postdetail
            comment.save()
            return redirect('postdetails', pk=postdetail.id)

    return render (request, 'posts/post-details.html', {'profile': profile, 'postdetail': postdetail, 'form':form})


@login_required(login_url="login")
def upload(request):
    profile=request.user.profile
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = profile
            post.save()
            return redirect('timeline')

    context = {'form':form}
    return render(request, 'posts/upload.html', context)


@login_required(login_url="login")
def deletePost(request, pk):
    profile=request.user.profile
    post = profile.post_set.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('timeline')
    context={'post':post}
    return render(request, 'posts/delete.html', context)


@login_required(login_url="login")
def likePost(request, pk):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else: like.value = 'Like'

        like.save()
    
        return HttpResponseRedirect(reverse('postdetails', args=[str(pk)]))


