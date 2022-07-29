from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Brsbook

# Create your views here.

def index(request):
    posts = Brsbook.objects.all()
    return render(request, '../templates/brs_app/index.html', {'posts': posts})



def detail(request, post_id):
    post = get_object_or_404(Brsbook, pk=post_id)
    return render(request, '../templates/brs_app/detail.html', {'post' : post})
''''
def new(request):
    return render(request, 'new.html')
'''

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
        return redirect('/brs_app/detail/' + str(post.id))
    else:
        return render(request, '../templates/brs_app/new.html')

def home(request):
    return render(request, '../templates/brs_app/index.html')

'''''
def edit(request, post_id):
    # 매개변수로 전달받은 id에 해당하는 post 객체를 불러온다.
    post = get_object_or_404(Brsbook, pk=post_id)
    # 딕셔너리 형태로 template에 전달한다. 전달한 쿼리셋은 수정화면에서 이전에 저장되어있던 데이터를 그대로 담기위해 사용된다.
    return render(request, 'edit.html', {'post' : post})
'''

def update(request, post_id):
    if(request.method == "POST"):
    # 매개변수로 전달받은 id에 해당하는 post 객체를 불러온다.
        post = get_object_or_404(Brsbook, pk=post_id)
    # post객체의 title에 GET 방식으로 요청된 name속성값이 'title'인 input 태그 내의 값을 저장한다.
        post.title = request.POST['title']
    # post객체의 content에 GET 방식으로 요청된 name속성값이 'content'인 input 태그 내의 값을 저장한다.
        post.content = request.POST['content']
    # 데이터베이스에 저장한다.
        post.category = request.POST['category']
        post.pub_date = timezone.datetime.now()
        post.cost = request.POST['cost']
        post.comment = request.POST['comment']
        post.user = request.user
        post.save()
    # 지정한 주소로 리다이렉트한다.
        return redirect('/brs_app/detail/' + str(post.id))
    else:
        post = get_object_or_404(Brsbook, pk=post_id)
        return render(request, '../templates/brs_app/edit.html', {'post' : post})
    
def delete(request, post_id):
    # 삭제할 레코드의 id 값을 get_object_or_404 메소드의 파라미터로 전달
    get_object_or_404(Brsbook, pk=post_id).delete()

    # redirect 메소드로 삭제 후에 되돌아갈 페이지를 지정
    return redirect('/')

