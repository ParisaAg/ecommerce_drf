from django.urls import path
from .views import hello
from .import views

urlpatterns = [
    path('',views.hello,name='hello'),
]
