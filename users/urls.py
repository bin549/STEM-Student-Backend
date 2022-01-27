from django.urls import path
from users import views


urlpatterns = [
    path('getAllUsers/', views.AllUsers.as_view()),
]
