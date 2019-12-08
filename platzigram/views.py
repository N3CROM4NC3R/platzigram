from django.http import HttpResponse

from datetime import datetime
import json


def hello_world(request):
    """ Return a Greeting and the datetime server """

    now = datetime.now().strftime('%b %dth, %Y - %H:%M')
    return HttpResponse('Oh hi,the current datetime server is :{now}'
    .format(now=str(now)))

def sort_numbers(request):
    """ Return a list of sorted numbers from GET """
    numbers = request.GET["numbers"]

    sorted_numbers = sorted([int(i) for i in
    numbers.split(',')])


    data ={
        "status":"ok",
        "numbers":sorted_numbers,
        "message":"The numbers was sorted sucessfully."
    }

    return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )

def register(request,name,age):
    """ Returns a Message about if the user is allowed register in platzigram """

    if age <= 12:
        message = "Sorry {},but you do not allowed register here.".format(name)
    else:
        message = "Welcome {name},Your age is {age}.".format(
            name=name.capitalize(),
            age=age
        )

    return HttpResponse(message)
