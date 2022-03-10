from django.urls import path
from homework import views


urlpatterns = [
    path('getAllHomework/', views.AllHomework.as_view()),
    path('getSelectedCourseHomeworks/<str:course_id>/', views.getSelectedCourseHomeworks),
    path('addHomework/', views.addHomework),
    path('loadHomeworks/', views.loadHomeworks),
    path('deleteHomework/', views.deleteHomework),
    path('getExecutionsById/<str:homework_id>/', views.getExecutionsById),
    path('setExecutionScore/', views.setExecutionScore),
    path('getExecutionExcellentById/<str:execution_id>/', views.getExecutionExcellentById),
    path('getCheckedExecutions/', views.getCheckedExecutions),
    path('getExcellentExecutions/<str:homework_id>/', views.getExcellentExecutions),
    path('getExcellentExecutionUserNames/<str:homework_id>/', views.getExcellentExecutionUserNames),
    path('getHomeworkById/<str:homework_id>/', views.getHomeworkById),
    path('uploadHomework/', views.uploadHomework),
    path('loadExecution/', views.loadExecution),
    path('getUnfinishHomework/<str:user_id>/', views.getUnfinishHomework),
    path('loadCourseAllHomeworks/', views.loadCourseAllHomeworks),
    path('loadCourseUnfinishHomeworks/', views.loadCourseUnfinishHomeworks),
    path('loadCourseFinishHomeworks/', views.loadCourseFinishHomeworks),
    path('loadUserExecution/', views.loadUserExecution),
]
