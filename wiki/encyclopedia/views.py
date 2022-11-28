from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def mdrender(request, name):
    if util.get_entry(name) is not None:
        return render(request, "encyclopedia/generic.html", {
            "markdown": util.get_entry(name)
        })
    else:
        return HttpResponseRedirect("url 'index'")
