from django.urls import path
from .views import hello_world, les, les1, zdraste
app_name ='blog'
urlpatterns =[
    path("hello/", hello_world, name = 'home'),
    path("zdraste/",zdraste, name = 'about'),
    path("les/", les, name = 'les'),
    path("les1/<int:pk>/", les1, name = 'post')
]