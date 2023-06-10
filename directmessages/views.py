from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ThreadModel, MessageModel
from users.models import Profile
from django.db.models import Q
from .forms import ThreadForm, MessageForm

# Create your views here.

def listThreads(request):
    if request.method == 'GET':
     threads = ThreadModel.objects.filter(Q(user = request.user.profile) | Q(receiver = request.user.profile))

     context = {
        'threads': threads
     }

    return render(request, 'directmessages/inbox.html', context)


def createThread(request):
   if request.method == 'GET':
      form = ThreadForm()
      context = {
        'form': form
     }
      return render(request, 'directmessages/create_thread.html', context)

   if request.method == 'POST':
      form = ThreadForm(request.POST)
      username = request.POST.get('username')

      try:
         receiver = Profile.objects.get(username=username)
         if ThreadModel.objects.filter(user = request.user.profile, receiver = receiver).exists(): 
            thread = ThreadModel.objects.filter(user=request.user.profile, receiver=receiver)[0]
            return redirect('thread', pk=thread.pk)
         elif ThreadModel.objects.filter(user=receiver, receiver=request.user.profile).exists():
            thread = ThreadModel.objects.filter(user=receiver, receiver=request.user.profile)[0]
            return redirect('thread', pk=thread.pk)
         if form.is_valid():
            thread = ThreadModel(user=request.user.profile, receiver=receiver)
            thread.save()

            return redirect('thread', pk=thread.pk)
      except:
         return redirect('create-thread')
      
def thread(request, pk):
   if request.method == 'GET':
      form = MessageForm()
      thread = ThreadModel.objects.get(pk=pk)
      message_list = MessageModel.objects.filter(thread__pk__contains=pk)

      context = {
        'form': form,
        'thread': thread,
        'message_list': message_list
     }
      return render(request, 'directmessages/thread.html', context)
   
def createMessage(request, pk):
   if request.method == 'POST':
      thread = ThreadModel.objects.get(pk=pk)
      if thread.receiver == request.user.profile:
         receiver = thread.user
      else:
         receiver = thread.receiver
      message = MessageModel(thread=thread, sender_user=request.user.profile, receiver_user=receiver, body=request.POST.get('message'))
      message.save()
      return redirect('thread', pk=pk)