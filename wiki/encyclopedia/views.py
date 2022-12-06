import os
import markdown2
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util

# hmmm

class MyForm(forms.Form):
    user_markdown = forms.CharField()
    user_title = forms.CharField()


def index(request):

    search_text = request.GET.get("q", None)
    entries = util.list_entries()

    if search_text == None:
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })
    
    elif search_text not in entries:

        # Search for entries that contain substring of search and filter the rest
        culled_entries = list(filter(lambda x: search_text in x, entries))
        return render(request, "encyclopedia/search_results.html", {
            "entries": culled_entries
        })

    else:
        return mdrender(request, search_text)


def mdrender(request, entry_name):
    markdown_file = util.get_entry(entry_name)

    # Get markdown file if it exists otherwise return an error
    if markdown_file is not None:
        return render(request, "encyclopedia/generic_entry.html", {
            "markdown": markdown_file
        })
    else:
        return render(request, "encyclopedia/error_markdown_file_not_found.html")

def create_page(request):

    # Validate form method and info
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user_markdown = form.cleaned_data['user_markdown']
            user_title = form.cleaned_data['user_title']

            util.save_entry(user_title, user_markdown)

            return HttpResponseRedirect(reverse("index"))

        

    else:
        form = MyForm()
        return render(request, "encyclopedia/create_page.html", {
            'form': form
        })

