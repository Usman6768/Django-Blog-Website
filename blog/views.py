from django.shortcuts import render


# Create your views here.

posts = [
    {
        'author' : 'Usman',
        'title' : 'Blog 1',
        'content': 'Hello this is my blog',
        'date_posted':'12-07-2024'
    },
    {
        'author' : 'Alex',
        'title' : 'Python tips',
        'content': 'Hello this is my pykit',
        'date_posted':'18-07-2018'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
