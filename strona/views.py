from django.shortcuts import render, get_object_or_404
from .models import Entry


def index(request):
    """Builds homepage. Much explanation"""
    return render(request, "stasiooo/index.html")

def post_show(request, id):
    """Shows a blog post."""
    bpost = get_object_or_404(Entry, pk=id)
    return render(request, "stasiooo/post.html", {'post': bpost})
