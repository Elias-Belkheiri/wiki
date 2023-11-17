from django.shortcuts import render, redirect
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

def search(request):
    q = request.POST["q"]
    entries = util.list_entries()
    matched_entries = [e for e in entries if q in e]
    if (q in matched_entries):
        return redirect('entry', title=q)
    if (matched_entries):
        return render(request, "encyclopedia/index.html", {
            "entries": matched_entries,
            "title": "matched queries"
        })
    return render(request, "encyclopedia/index.html", {
        "body": "Entry Not Found",
        "title": matched_entries})

def add(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/form.html")
    elif request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        entries = util.list_entries()
        matched_entries = [e for e in entries if e == title]
        if (len(matched_entries) or len(title) == 0 or len(content) == 0):
            return HttpResponse("Invalid Entry")
        util.save_entry(title, content)
        return redirect('entry', title=title)
