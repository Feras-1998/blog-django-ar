from django.http import request
from django.shortcuts import render
from .models import Post

# posts = [{
#     'titale': 'التدوينة 1',
#     'contant': 'نص تجريبي',
#     'post_date': '15-3-2020',
#     'author': 'احمد'
# }, {
#     'titale': 'التدوينة 2',
#     'contant': 'نص تجريبي',
#     'post_date': '30-4-2020',
#     'author': 'فراس'
# }, {
#     'titale': 'التدوينة 3',
#     'contant': 'نص تجريبي',
#     'post_date': '3-3-2015',
#     'author': 'عمر'
# }, {
#     'titale': 'التدوينة 4',
#     'contant': 'نص تجريبي',
#     'post_date': '15-9-2016',
#     'author': 'محمد'
# }, {
#     'titale': 'التدوينة 5',
#     'contant': 'نص تجريبي',
#     'post_date': '1-1-2020',
#     'author': 'عبد'
# }]


def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def about(request):
    context = {'title': 'من أنا'}
    return render(request, 'blog/about.html', context)
