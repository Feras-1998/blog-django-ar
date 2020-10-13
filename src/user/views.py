from django.core.checks import messages
from .forms import UserCreationForm, LoginForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data['username']

            messages.success(request, f'تهانينا {username} لقد تمت عملية التسجيل بنجاح')

            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'title': 'التسجيل',
        'form': form,
    }

    return render(request, 'user/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        name = request.POST['username']
        word = request.POST['password']
        user = authenticate(request, username=name, password=word)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'هنالك خطأ في اسم المستخم او كلمة المرور')
    else:
        form = LoginForm()

    context = {
        'title': 'تسجيل الدخول',
        'form': form,
    }

    return render(request, 'user/login.html', context)

def logout_user(request):
    logout(request)
    context = {
        'title': 'تسجيل الخروج'
    }

    return render(request, 'user/logout.html', context)

def profile(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'title': 'الملف الشخصي',
        'posts': posts,
    }

    return render(request, 'user/profile.html', context)
