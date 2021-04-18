from django.shortcuts import render, HttpResponse


def homepage(reguest):
    return HttpResponse("hello world!")


def test(reguest):
    return render(reguest, "test.html")