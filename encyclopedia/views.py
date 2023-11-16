from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "encyclopedia"
    })

def entry(request, title):
    body = util.get_entry(title)
    if body == None:
        body = "Entry Not Found :("
    return render(request, "encyclopedia/index.html", {
    "body": body,
    "title": title})