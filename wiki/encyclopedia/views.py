from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def mdrender(request, entry_name):
    if util.get_entry(entry_name) is not None:
        return render(request, "encyclopedia/generic.html", {
            "markdown": util.get_entry(entry_name)
        })
    else:
        return HttpResponseRedirect("url 'index'")
