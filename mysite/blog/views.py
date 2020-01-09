from django.shortcuts import render
from django.http import HttpResponse

po = [
    {
        'author': 'CoreyMS',
        'title': 'blog Post 1',
        'content': 'First post content',
        'date_posted': 'Augus'
    },
    {
        'author': 'Jane',
        'title': 'blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August'
    }
]
def home(request):
    context = {
        'posts': po
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
