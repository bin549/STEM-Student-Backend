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
    path('getUserSelection/<str:user_id>/', views.getUserSelection),
    path('getCourseLessons/<str:course_id>/', views.getCourseLessons),
    path('getUserCollection/<str:user_id>/', views.getUserCollection),
    path('getOwnerCourse/<str:user_id>/', views.getOwnerCourse),
    path('course_student/<slug:course_slug>/', views.SelectionUser.as_view()),
]
