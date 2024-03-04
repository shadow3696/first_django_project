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
        'author': 'ali',
        'title': 'django',
        'content': 'im power source',
        'date_post': '2020 / 12 / 20',
    },
]

# start views  # inja ma omadim func haiee ro tarif kardim ke ba ejra shodan chizi ro be namayesh mizaran
def Home(request):
    return render(request, 'blog/home.html')

def About(request):
    return render(request, 'blog/about.html')
# end views
