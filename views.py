from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect
from .forms import PostForm
from .forms import DoctorForm
from .forms import DeleteDoctorForm
from .forms import NurseForm
from .forms import ClientForm
from .forms import HistoryForm
from django.db.models import*
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
    doctors_count = Doctor.objects.count()
    top_qualification = Doctor.objects.filter(qualification = 'Высшая').count()
    num_admission_department = Doctor.objects.filter(department = 'Приемное').count()
    num_therapeutic_department = Doctor.objects.filter(department = 'Терапевтическое').count()
    return render(request, 'myapp/mydoctor.html', {'doctors': doctors, 'doctors_count': doctors_count, 'top_qualification': top_qualification, 'num_admission_department': num_admission_department, 'num_therapeutic_department':num_therapeutic_department})
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

def mynurse(request):
    nurses = Nurse.objects.order_by('name')
    nurses_count = Nurse.objects.count()
    num_admission_department = Nurse.objects.filter(department = 'Приемное').count()
    num_therapeutic_department = Nurse.objects.filter(department = 'Терапевтическое').count()
    return render(request, 'myapp/mynurse.html', {'nurses': nurses,'num_therapeutic_department':num_therapeutic_department, 'num_admission_department':num_admission_department, 'nurses_count': nurses_count})


def newnurse(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            nurse = form.save(commit = False)
            nurse.save()
            return redirect('mynurse')
    else:
        form = NurseForm()
    return render(request, 'myapp/newnurse.html', {'form': form})


def myclient(request):
    clients = Client.objects.order_by('name')
    clients_count = Client.objects.count()
    return render(request, 'myapp/myclient.html', {'clients': clients,'clients_count': clients_count })

def newclient(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit = False)
            client.save()
            return redirect('myclient')
    else:
        form = ClientForm()
    return render(request, 'myapp/newclient.html', {'form': form})

def myhistory(request):
    histories = History.objects.order_by('history_number')
    return render(request, 'myapp/myhistory.html', {'histories': histories})

def newhistory(request):
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit = False)
            history.save()
            return redirect('myhistory')
    else:
        form = HistoryForm()
    return render(request, 'myapp/newhistory.html', {'form': form})
