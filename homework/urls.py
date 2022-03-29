from django.urls import path
from homework import views


urlpatterns = [
    path('addHomework/', views.addHomework),
    path('deleteHomework/', views.deleteHomework),
    path('getAllHomework/', views.AllHomework.as_view()),
    path('loadHomeworks/', views.loadHomeworks),
    path('loadCourseAllHomeworks/', views.loadCourseAllHomeworks),
    path('getHomeworks/<str:user_id>/', views.getHomeworks),
    path('getUnfinishHomework/<str:user_id>/', views.getUnfinishHomework),
    path('getHomeworkById/<str:homework_id>/', views.getHomeworkById),
    path('uploadHomework/', views.uploadHomework),
    path('loadExecution/', views.loadExecution),
    path('loadUserExecution/', views.loadUserExecution),
    path('setExecutionScore/', views.setExecutionScore),
    path('getExecutionImages/<str:execution_id>/', views.getExecutionImages),
    path('getCheckedExecutions/', views.getCheckedExecutions),
    path('getExcellentExecutions/<str:homework_id>/', views.getExcellentExecutions),
    path('getExcellentExecutionUserNames/<str:homework_id>/', views.getExcellentExecutionUserNames),
    path('loadCourseUnfinishHomeworks/', views.loadCourseUnfinishHomeworks),
    path('loadCourseFinishHomeworks/', views.loadCourseFinishHomeworks),
    path('getSelectedCourseHomeworks/<str:course_id>/', views.getSelectedCourseHomeworks),
    path('getExecutionsById/<str:homework_id>/', views.getExecutionsById),
    path('getExecutionExcellentById/<str:execution_id>/', views.getExecutionExcellentById),
]
