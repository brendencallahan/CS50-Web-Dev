from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def mdrender(request, entry_name):
    markdown_file = util.get_entry(entry_name)
    if markdown_file is not None:
        return render(request, "encyclopedia/generic.html", {
            "markdown": markdown_file
        })
    else:
        return HttpResponseRedirect("url 'index'")
