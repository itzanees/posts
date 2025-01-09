from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Post


# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

def signup(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form':form})


@login_required(login_url="/login")
def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('viewpost')
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html', {'form':form})

@login_required(login_url='/login')
def viewpost(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main/viewpost.html', {'posts':posts})

@login_required(login_url='/login')
def editpost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if post and post.author == request.user:
                edit = form.save(commit=False)
                edit.author=request.user
                edit.save()
                return redirect('viewpost')
    else:
        form = PostForm(instance=post)
        path=f"/post/edit/{pk}"
    return render(request, 'main/create_post.html', {'form':form, 'path':path})

@login_required(login_url='/login')
def deletepost(request, pk):
    post = Post.objects.get(pk=pk)
    if post and post.author == request.user:
        post.delete()
    return redirect('viewpost')