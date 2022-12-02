from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

# hmmm

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def mdrender(request, entry_name):
    markdown_file = util.get_entry(entry_name)
    if markdown_file is not None:
        return render(request, "encyclopedia/generic_entry.html", {
            "markdown": markdown_file
        })
    else:
        return render(request, "encyclopedia/error_markdown_file_not_found.html")

def search(request, search_text):
    if search_text in util.list_entries():
        return mdrender(request, search_text)
    else: 
        return render(request, "encyclopedia/error_markdown_file_not_found.html")