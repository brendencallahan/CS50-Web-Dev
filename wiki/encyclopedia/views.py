from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

# hmmm

def index(request):
    
    if request.GET.get("q", None) == None:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    
    else:
        return mdrender(request, request.GET.get("q"))


def mdrender(request, entry_name):
    markdown_file = util.get_entry(entry_name)
    if markdown_file is not None:
        return render(request, "encyclopedia/generic_entry.html", {
            "markdown": markdown_file
        })
    else:
        return render(request, "encyclopedia/error_markdown_file_not_found.html")
