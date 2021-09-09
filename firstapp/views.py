from django.shortcuts import render
from firstapp.models import Person
from django.http import JsonResponse

# Create your views here.

def getPeople(request):
    result=Person.objects.all()
    return JsonResponse({'people': list(result.values())
    })