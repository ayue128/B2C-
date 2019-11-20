from django.shortcuts import render

# Create your views here.
from common.models import Types


def loadinfo(request):
    context = {}
    context['types'] = Types.objects.all()
    return context