from django.urls import path
from .views import student, goodbye

urlpatterns = [
   path("", student),
   path("goodbye/", goodbye)
]
