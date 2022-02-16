from django.urls import path
from homework import views


urlpatterns = [
    path('getAllHomework/', views.AllHomework.as_view()),
    path('getSelectedCourseHomeworks/<str:course_id>/', views.getSelectedCourseHomeworks),
    path('addHomework/', views.addHomework),
    path('loadHomeworks/', views.loadHomeworks),
    path('deleteHomework/', views.deleteHomework),
]
 