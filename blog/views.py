from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return render(request,'index.html',{ "active":"active" })

def zdraste(request):
    return render(request,'about.html',{ "active":"active" })

# def text(request):
#     a = 'tsaffjajsfngjknkajf;sd;'
#     return render(request,'index.html',{'text':a})   

# def text2(request):
#     b ='zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxvmkdssnvodsnvjdsnvjodsnvojdsnvoisdnvoidsnvoisdnoiv'
#     return render(request,'index.html',{'text2':b})

def les(request):
    return render(request,'contact.html', { "active":"active" })
def les1(request):
    return render(request,'post.html', { "active":"active" })            