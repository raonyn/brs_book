from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Brsbook

# Create your views here.

def index(request):
    posts = Brsbook.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create(request):
    if(request.method == 'POST'):
        post = Brsbook()
        post.title = request.POST['title']
        post.category = request.POST['category']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.cost = request.POST['cost']
        post.comment = request.POST['comment']
        post.user = request.user
        post.save()
        return redirect('/detail/' + str(post.id))
     #   return render(request, 'index.html')
    else:
        return render(request, 'error.html')

def detail(request, post_id):
    post = get_object_or_404(Brsbook, pk=post_id)
    return render(request, 'detail.html', {'post' : post})

def new(request):
    return render(request, 'new.html')

def home(request):
    return render(request, 'index.html')

def delete(request, post_id):
    # 삭제할 레코드의 id 값을 get_object_or_404 메소드의 파라미터로 전달
    get_object_or_404(Brsbook, pk=post_id).delete()

    # redirect 메소드로 삭제 후에 되돌아갈 페이지를 지정
    return redirect('/')
