from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title' : 'Mont Blanc',
        'user' : {
            'name' : 'Maria Fernanda',
            'picture' : 'https://picsum.photos/60/?image=1027',
        },
        'timestamp' : datetime.now().strftime('%d %b %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/800/600/?image=1036',
    },
    {
        'title' : 'Via Lactea',
        'user' : {
            'name' : 'You',
            'picture' : 'https://picsum.photos/60/?image=1005',
        },
        'timestamp' : datetime.now().strftime('%d %b %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/800/600/?image=903',
    },
    {
        'title' : 'Slipknot',
        'user' : {
            'name' : 'Killpop',
            'picture' : 'https://picsum.photos/60/?image=883',
        },
        'timestamp' : datetime.now().strftime('%d %b %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/800/600/?image=1076',
    }
]

def list_posts(request):
    return render(request, 'feed.html', {'posts' : posts})