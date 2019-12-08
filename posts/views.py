""" Posts views """
# Django
from django.shortcuts import render

#utilities
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

def list_posts(request):
    return render(request,'feed.html',{'posts':posts})
