from django.urls import path
from course import views


urlpatterns = [
    path('getAllCourse/', views.AllCourse.as_view()),
    path('getAllRecomendedCourse/', views.AllRecomendedCourse.as_view()),
    path('getAllGenre/', views.AllGenre.as_view()),
    path('getAllSelection/', views.AllSelection.as_view()),
    path('getAllCollection/', views.AllCollection.as_view()),
    path('courses/<slug:genre_slug>/<slug:course_slug>/', views.CourseDetail.as_view()),
    path('courses/<slug:genre_slug>/', views.GenreDetail.as_view()),
    path('getUserSelection/<str:pk>/', views.getUserSelection),
]
