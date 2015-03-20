from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    context = RequestContext(request, {})
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render(context))

def about(request):
    context = RequestContext(request, {})
    template = loader.get_template('core/about.html')
    return HttpResponse(template.render(context))