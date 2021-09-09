from django.urls import path, include
from firstapp.views import getPeople


urlpatterns = [
    path('list/', getPeople, name='people-list')
]