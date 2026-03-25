from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the blog home tarun chauhan page!")


def about(request):
    return HttpResponse("Welcome to the blog about page!")


def contact(request):
    return HttpResponse("Welcome to the blog contact page!")