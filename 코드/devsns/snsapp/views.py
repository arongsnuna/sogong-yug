from turtle import pos
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

def main(request):
    return render(request, 'main1.html')

def home(request):
    posts = Post.objects.all()
    return render(request, 'main2.html', {'posts':posts})

def postcreate(request):
    # request method가 post일 경우
    # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # request method가 get일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

# 상세보기
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})

# 삭제하기
def remove(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home')

# 수정하기
def edit(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == "POST":
    post.title = request.POST['title']
    post.price = request.POST['price']
    post.size = request.POST['size']
    post.season = request.POST['season']
    post.cloth_type = request.POST['cloth_type']
    post.washType = request.POST['washType']
    post.temperature = request.POST['temperature']
    post.drycleaning = request.POST['drycleaning']
    post.repair = request.POST['repair']
    
    try:
      post.mainphoto = request.FILES['image']
    except:
      post.image = None
    post.save()
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})
  else:
    form = PostForm()
    return render(request, 'edit.html', {'form':form})
