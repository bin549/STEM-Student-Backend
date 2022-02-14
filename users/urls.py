from django.urls import path
from users import views


urlpatterns = [
    path('getAllUsers/', views.AllUsers.as_view()),
    path('getUserInfo/<str:pk>/', views.getUserInfo),
    path('getUserTypeName/', views.getUserTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('addUser/', views.addUser),
]
