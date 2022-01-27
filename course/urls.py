from django.urls import path
from course import views


urlpatterns = [
    path('getAllCourse/', views.AllCourse.as_view()),
    path('getAllGenre/', views.AllGenre.as_view()),
    path('getAllSelection/', views.AllSelection.as_view()),
    path('getAllCollection/', views.AllCollection.as_view()),
]
