""" Posts views """
# Django
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.decorators import login_required
#Local
from users.models import Profile

# Utilities
from datetime import datetime
# Create your views here.

posts = [
    {
        'title':'Mont Blac',
        "user":{

            'name':'Yesica Cortes',
            'picture':'https://picsum.photos/60/60/?image=1027',
        },
        'photo':'https://picsum.photos/200/300/?image=1036',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M'),
    },
    {
        'title':'Via Làctea',
        "user":{

            'name':'C. Vander',
            'picture':'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M'),
        'photo':'https://picsum.photos/200/300/?image=903',
    },
    {
        'title':'Nuevo auditorio',
        "user":{

            'name':'Thepianartist',
            'picture':'https://picsum.photos/60/60/?image=883'
        },
        'photo':'https://picsum.photos/200/300/?image=1076',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M'),

    }
]


@login_required()
def list_posts(request):
    user = request.user
    profile = Profile.objects.get(user_id = user.id)
    return render(request,'posts/feed.html',{'posts':posts,'profile': profile})
