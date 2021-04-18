from django.shortcuts import render, HttpResponse


def homepage(reguest):
    return HttpResponse("hello world!")


def test(reguest):
    return render(reguest, "test.html")

def second(request):
    return HttpResponse("test 2 page")