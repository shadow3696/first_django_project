from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ali',
        'title': 'django',
        'content': 'im power source',
        'date_post': '2020 / 12 / 20',
    },
    {
    'author': 'mohammad',
    'title': 'reactpy',
    'content': 'im end power source',
    'date_post': '2022 / 5 / 00',
    },
    {
    'author': 'ahmad',
    'title': 'python',
    'content': 'im start power source',
    'date_post': '2018 / 10 / 30',
    },
]

# start views  # inja ma omadim func haiee ro tarif kardim ke ba ejra shodan chizi ro be namayesh mizaran
def Home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html')

def About(request):
    return render(request, 'blog/about.html')
# end views
