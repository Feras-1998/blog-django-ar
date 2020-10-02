from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import NewComment

def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    context = {'title': 'من أنا'}
    return render(request, 'blog/about.html', context)


def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    comment_form = NewComment()
    new_comment = None
    
    context = {
        'title': post.title,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
        else:
            comment_form = NewComment()

    return render(request, 'blog/detail.html', context)
