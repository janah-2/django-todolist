from django.urls import path
from . import views


urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("registered/", views.registered, name="registered"),
path("loggedin/", views.loggedin, name="loggedin"),
path("loggedout/", views.loggedout, name="loggedout"),
path("view/", views.view, name="view"),
path("view/deletelists/<str:pk>/", views.deleteList, name="deletelist"),
path("delete/<str:pk>/<str:id>/", views.deleteTask, name="deletetask"),
]