from django.shortcuts import render

# Cfrom django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
