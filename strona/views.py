from django.shortcuts import render


def index(request):
    """Builds homepage. Much explanation"""
    return render(request, "stasiooo/index.html")
