from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Flowers',
        'user': {
            'name': 'Nicole Kilby',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=152',
    },
    {
        'title': 'Love bridge',
        'user': {
            'name': 'Kevin Zarama',
            'picture': 'https://picsum.photos/60/60/?image=338'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/336/600/600',
    },
    {
        'title': 'Dogs',
        'user': {
            'name': 'Christian Pechene',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/237/600/600',
    },
    {
        'title': 'Nature',
        'user': {
            'name': 'Natalia Burbano',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=161',
    }
]

def list_posts(request):
    return render(request, 'feed.html', {'posts':posts})