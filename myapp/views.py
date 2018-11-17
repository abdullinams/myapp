from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Doctor
from django.shortcuts import redirect
from .forms import PostForm
from .forms import DoctorForm
from .forms import DeleteDoctorForm
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myapp/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myapp/post_edit.html', {'form': form})
def mydoctor(request):
    doctors = Doctor.objects.order_by('name')
    return render(request, 'myapp/mydoctor.html', {'doctors': doctors})
def newdoctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit = False)
            doctor.save()
            return redirect('mydoctor')
    else:
        form = DoctorForm()
    return render(request, 'myapp/newdoctor.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myapp/post_edit.html', {'form': form})

def deletedoctor(request):
    if request.method == "POST":
        form = DeleteDoctorForm(request.POST)
        if form.is_valid():
            doctor = Doctor.objects.get(name = form.get(name))
            doctor.delete()
            return redirect('mydoctor')
    else:
        form = DeleteDoctorForm()
    return render(request, 'myapp/deletedoctor.html', {'form': form})
