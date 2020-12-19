from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .forms import HeroForm
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import HeroSerializer
from .models import Hero
from django.template import loader


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

def index(request):
    queryset = Hero.objects.all().order_by('id')
    template = loader.get_template('myapi/index.html')
    context = {
        'queryset': queryset,
    }
    return HttpResponse(template.render(context, request))

def addnew(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('alias'):
                post=Hero()
                post.name= request.POST.get('name')
                post.alias= request.POST.get('alias')
                post.save()
                queryset = Hero.objects.all().order_by('id')
                template = loader.get_template('myapi/index.html')
                context = {
                    'queryset': queryset,
                }
                return HttpResponse(template.render(context, request))

        else:
                return render(request,'myapi/addnew.html')
            
def delete(request, id):
    note = get_object_or_404(Hero,pk =id).delete()
    queryset = Hero.objects.all().order_by('id')
    template = loader.get_template('myapi/index.html')
    context = {
                    'queryset': queryset,
                }
    return HttpResponse(template.render(context, request))

def edit(request, id):
    queryset = Hero.objects.get(pk=id)
    template = loader.get_template('myapi/update.html')
    context = {
                    'queryset': queryset,
                }
    
    return HttpResponse(template.render(context, request))

def update(request, id):
    hero = Hero.objects.get(pk=id)
    heroform = HeroForm(request.POST or None, instance=hero)
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('alias'):
            heroform.name= request.POST.get('name')
            heroform.alias= request.POST.get('alias')
            heroform.save()
            return redirect('index')
        else:
            context ={'queryset',heroform}
            template='myapi/update.html'
            return render(request,template,context)  
        
    
    