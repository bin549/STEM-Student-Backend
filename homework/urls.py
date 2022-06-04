from django.urls import path
from homework import views


urlpatterns = [
    path('getAllHomework/', views.AllHomework.as_view()),
    path('getUnfinishHomework/<str:user_id>/', views.getUnfinishHomework),
    path('uploadHomework/', views.uploadHomework),
    path('getHomeworkId/<str:execution_id>/', views.getHomeworkId),
    path('loadCourseUnfinishHomeworks/', views.loadCourseUnfinishHomeworks),
    path('loadCourseFinishHomeworks/', views.loadCourseFinishHomeworks),
    path('getSelectedCourseHomeworks/<str:course_id>/', views.getSelectedCourseHomeworks),
    path('loadUserExecution/', views.loadUserExecution),
    path('getExecutionsById/<str:homework_id>/', views.getExecutionsById),
    path('getExecutionExcellentById/<str:execution_id>/', views.getExecutionExcellentById),
    path('getCourseId/<str:homework_id>/', views.getCourseId),
    path('getExecutionById/<str:execution_id>/', views.getExecutionById),



    path('getHomeworks/<str:user_id>/', views.AssignmentAPI.as_view()),
    path('Homework/getById/', views.AssignmentAPI.as_view()),
    path('Homework/getByUserId/', views.AssignmentAPI.as_view()),
    path('Homework/getByCourseId/', views.AssignmentAPI.as_view()),
    path('Homework/getByFinish/', views.AssignmentAPI.as_view()),
    path('Execution/getAll/', views.ExecutionAPI.as_view()),
    path('Execution/get/', views.ExecutionAPI.as_view()),
    path('getExecutionImages/<str:execution_id>/', views.MediaAPI.as_view()),
    path('Star/create/', views.StarAPI.as_view()),
    path('Star/delete/', views.StarAPI.as_view()),
    path('Star/get/', views.StarAPI.as_view()),
    path('Star/getAll/', views.StarAPI.as_view()),


    path('createActivityLog/<str:execution_id>/', views.LogAPI.as_view()),
]
