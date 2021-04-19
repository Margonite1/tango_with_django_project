from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Rango says hey there partner! (<a href='/rango/about/'>About</a>)")
def index(request):
    # Construct a dictionary to pass to the templates engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the templates!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the templates we wish to use.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # Construct a dictionary to pass to the templates engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the templates!
    context_dict = {'boldmessage': 'This tutorial has been put together by Martin Bowmaker'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the templates we wish to use.
    return render(request, 'rango/about.html', context=context_dict)
def static(request):
    return HttpResponse("Rango says here is the static page.  <a href='/rango/'>Index</a>")
def rangojpg(request):
    return render(request,'rango/image.html')
