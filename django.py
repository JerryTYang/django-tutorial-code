// for views.py
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world!”)

// for boards/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]

// for sesite/urls

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

// for creating models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.PROTECT)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.PROTECT)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.PROTECT)


// for displaying on server

from django.http import HttpResponse
from .models import Board

def index(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)

/*
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    {% for board in boards %}
      {{ board.name }} <br>
    {% endfor %}

  </body>
</html>
*/
