from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import OwnEntryForm


def index(request):
    """Builds homepage. Much explanation"""
    return render(request, "stasiooo/index.html")


def post_show(request, pid):
    """Shows a blog post."""
    bpost = get_object_or_404(Entry, pk=pid)
    return render(request, "stasiooo/post.html", {"post": bpost})


def post_edit(request, pid):
    """Applies edits to a blog post or shows the editing form."""
    bpost = get_object_or_404(Entry, pk=pid)
    if request.method == "POST":
        form = OwnEntryForm(request.POST, initial={"title": bpost.title, "content": bpost.content, "publication_time": bpost.publication_time})
        if form.is_valid():
            if bpost.author == request.user and form.has_changed():
                bpost.title = form.cleaned_data["title"]
                bpost.content = form.cleaned_data["content"]
                bpost.publication_date = form.cleaned_data["publication_time"]
                bpost.save()
                return HttpResponseRedirect(reverse("post_show", args=(pid,)))
    else:
        form = OwnEntryForm(initial={"title": bpost.title, "content": bpost.content, "publication_time": bpost.publication_time})
    return render(request, "stasiooo/post_edit.html", {"post": bpost, "form": form})
