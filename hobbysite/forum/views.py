from django.http import HttpResponse

def apology(request):
    return HttpResponse("Our 5th group member will work on this at their own time, sorry! <a href='/'>Go Back</a>")