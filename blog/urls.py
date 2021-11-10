from django.urls import path
from .views import hello_world, les, les1, zdraste
app_name ='blog'
urlpatterns =[
    path("hello/", hello_world),
    path("zdraste/",zdraste),
    path("les/", les, name = 'les'),
    path("les1/", les1)
]