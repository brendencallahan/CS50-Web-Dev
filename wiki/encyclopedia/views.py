from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

# hmmm

def index(request):

    search_text = request.GET.get("q", None)
    entries = util.list_entries()

    if search_text == None:
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })
    
    elif search_text not in entries:

        culled_entries = list(filter(lambda x: search_text in x, entries))
        return render(request, "encyclopedia/search_results.html", {
            "entries": culled_entries
        })

    else:
        return mdrender(request, search_text)


def mdrender(request, entry_name):
    markdown_file = util.get_entry(entry_name)
    if markdown_file is not None:
        return render(request, "encyclopedia/generic_entry.html", {
            "markdown": markdown_file
        })
    else:
        return render(request, "encyclopedia/error_markdown_file_not_found.html")

def create_page(request):
    if request.method == 'POST':
        return render(request, "")

    else:
        return render(request, "encyclopedia/create_page.html", {
        }) 