from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_name>", views.mdrender, name="entry_name"),
    path("create_page/", views.create_page, name="create_page")
]
