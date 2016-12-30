"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render

from django.views.generic import TemplateView
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from . import models

from app.models import Registern
from app.models import car_info

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def a(request):
	txt="Hello"
	return HttpResponse(txt)
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html')

    
    
class First1(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'First.html')    
    
    
    

def demo(request):
    n = request.POST.get("Name",' ')
    u = request.POST.get("UName",' ')
    p = request.POST.get("Password",' ')
    r = request.POST.get("CPassword",' ')
    
    

#search = car_info(Name)
    queryset1 = models.Registern(Name=n, Username=u, Password=p,CPassword=r)
    

    queryset1.save()
    
    data = {
        'queryset1': queryset1,

    }
   
    return render(request, './Registration.html', data)


def archive(request):
    posts = models.Registern.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

def archive1(request):
    ln = request.POST.get("lname",' ')
    lp = request.POST.get("lpwd",' ')  
    posts = models.Registern.objects.all() 

    for post in posts:
    
    
     if ln==post.Username and lp==post.Password:
        return render(request, './home.html')
    else:
        return render(request,'./login.html')
  
        
def Reg(request): 
        return render(request, './Registration.html')
    
def prin(request):
    postss = models.Registern.objects.all() 
    for ppost in postss:
      return HttpResponse(ppost.Username)
  
def car(request):
    n = request.POST.get("loc_id",' ')
    print(n)
    ad = request.POST.get("from_id",' ')
    print(ad)
    em = request.POST.get("to_id",' ')
    print(em)
    

#search = car_info(Name)
    queryset1 = models.car_info(location=n, from_id=ad, to=em)
    

    queryset1.save()
    
    data = {
        'queryset1': queryset1,

    }
   
    return render(request, './home.html', data)    

def success(request):
    posts = models.car_info.objects.all()
    t = loader.get_template("SuccesfulB.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))


        
def book(request): 
        return render(request, './home.html')
    
def logout(request): 
        return render(request, './login.html')   
    
    
def archive12(request):
    post1 = models.Registern.objects.all()
    t = loader.get_template("reg.html")
    c = Context({ 'post1': post1 })
    return HttpResponse(t.render(c))      

