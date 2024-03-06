from django.urls import path
from . import views

# This is the URL configuration file for the polls application.
# The `urlpatterns` list routes URLs to views.
# The `path()` function is passed four arguments,
# two required: route and view,
# and two optional: kwargs, and name.

# The route is a string that contains a URL pattern.

# The view is a view function that Django will call when the pattern is matched.

# The kwargs is an arbitrary keyword argument passed to the target view.

# The name is a name for the URL pattern, which makes it possible to refer to the
# pattern unambiguously from elsewhere in Django, especially from within templates.

urlpatterns = [
    path("", views.index, name="index"), # In this case, the route is an empty string, which means that the view will be called for the root URL.
]
