from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse("I am learning Django")


def hello(request: HttpRequest):
    return HttpResponse("Hello Django World!")
