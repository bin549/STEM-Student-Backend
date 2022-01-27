from django.urls import path
from homework import views


urlpatterns = [
    path('getAllHomework/', views.AllHomework.as_view()),
]
