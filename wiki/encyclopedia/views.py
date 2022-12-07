from markdown2 import Markdown
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib import messages

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

        markdowner = Markdown()
        markdown = markdowner.convert(markdown_file)

        return render(request, "encyclopedia/generic_entry.html", {
            "markdown": markdown,
            "entry_name": entry_name
        })
    else:
        return render(request, "encyclopedia/error_markdown_file_not_found.html")

def create_page(request):

    entries = util.list_entries()

    # Validate form method and info
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user_markdown = form.cleaned_data['user_markdown']
            user_title = form.cleaned_data['user_title']

            # Check if entry exists
            if user_title in entries:
                return render(request, "encyclopedia/error_title_taken.html")

            util.save_entry(user_title, user_markdown)

            return HttpResponseRedirect(reverse("index"))

        

    else:
        form = MyForm()
        return render(request, "encyclopedia/create_page.html", {
            'form': form
        })


def edit_page(request, entry_name):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user_markdown = form.cleaned_data['user_markdown']
            user_title = form.cleaned_data['user_title']

            if entry_name != user_title:
                util.delete_entry(entry_name)

            util.save_entry(user_title, user_markdown)

            url = reverse(mdrender, kwargs={'entry_name': user_title})
            return HttpResponseRedirect(url)
    

    else:
        markdown_file = util.get_entry(entry_name)
        form = MyForm()
        if markdown_file is not None:
            return render(request, "encyclopedia/edit_page.html", {
                "markdown": markdown_file,
                "entry_name": entry_name
            })
        else:
            return render(request, "encyclopedia/error_markdown_file_not_found.html")
