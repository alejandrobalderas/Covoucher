from django.urls import path

from . import views as home_views

app_name = "home"
urlpatterns = [
    path('', home_views.home_view, name="home"),
]
