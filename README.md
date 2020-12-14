# Django-Rest-Api
Django Rest Api  |  Django Version: 3.1.3


### Creare environment and your first project
- Create a directory
 `mkdir DjangoApp`  <br>
 
- Into the "DjangoApp" directory create a virtual environment 
`python -m venv apienv`  <br>

- Active the environment
`apienv/Scripts/activate` (optional: run `Set-ExecutionPolicy RemoteSigned` in windows powershell as Administrator if scripts is disabled) <br>

- Install Django
`pip install django`  <br>

- Create your first Django app
`django-admin startproject app`  <br>

- Get into the app directory
`cd app`  <br>

- Run the project
`python manage.py runserver`  <br>

 Bingo!  app is running, Now   <br>

- Create a requirements.txt file
`pip freeze > requirements.txt`  <br>

- Add a Django .gitignore file  <br>

- Add git using `git init`  and pust the project to git if you want

<br><br>

### Creare API view
- Create an app
 `python manage.py startapp blogapi`  <br>

- install Django REST framework
 `pip install djangorestframework`  <br>

- Register blogapi and rest_framework at **settings.py**
```
INSTALLED_APPS = [
    ...
    'blogapi',
    'rest_framework',
]
```
<br>

- Create a model class at **blogapi/models.py**
```
#models.py

 class Post(models.Model):

    STATUS = (
        ('draft', 'draft'),
        ('published', 'published'),)

    title = models.CharField(max_length=80, unique=True, db_index=True)
    body = models.TextField(default = "draft")
    status = models.CharField(max_length=10, null=False, choices=STATUS)
    publish_date = models.DateField(
        auto_now_add=True)  # auto_now_add will set the timezone.now() only when the instance is created
    update_date = models.DateField(auto_now=True,
                                   null=False)  # auto_now will update the field everytime the save method is called

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['publish_date']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_details", kwargs={"slug": self.title})
```

<br>

- Register models at **blogapi/admin.py**
```
from blogapi.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'status', 'publish_date', 'update_date')

admin.site.register(Post, PostAdmin)
```

<br>

- Add serializer at **blogapi** directory
```
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')
```

<br>

- Add class-based view at **blogapi/views.py** and modify **urls.py**

```
#views.py

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer
```

```
#urls.py

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from blogapi import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
