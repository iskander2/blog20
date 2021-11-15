from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def hello_world(request):
    posts = Post.objects.all()
    return render(request,'index.html',{ "home":"active", "posts": posts })

def zdraste(request):
    return render(request,'about.html',{ "about":"active" })

# def text(request):
#     a = 'tsaffjajsfngjknkajf;sd;'
#     return render(request,'index.html',{'text':a})   

# def text2(request):
#     b ='zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxvmkdssnvodsnvjdsnvjodsnvojdsnvoisdnvoidsnvoisdnoiv'
#     return render(request,'index.html',{'text2':b})

def les(request):
    return render(request,'contact.html', { "contact":"active" })
def les1(request):
    return render(request,'post.html', { "post":"active" })            