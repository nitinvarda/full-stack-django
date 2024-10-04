from django.urls import path,include
from students import views


urlpatterns = [
    path("", views.students)
]