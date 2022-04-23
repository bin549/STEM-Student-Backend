from django.urls import path
from homework import views


urlpatterns = [
    path('deleteHomework/', views.deleteHomework),
    path('getAllHomework/', views.AllHomework.as_view()),
    path('getUnfinishHomework/<str:user_id>/', views.getUnfinishHomework),
    path('uploadHomework/', views.uploadHomework),
    path('getHomeworkId/<str:execution_id>/', views.getHomeworkId),
    path('loadCourseUnfinishHomeworks/', views.loadCourseUnfinishHomeworks),
    path('loadCourseFinishHomeworks/', views.loadCourseFinishHomeworks),
    path('getSelectedCourseHomeworks/<str:course_id>/', views.getSelectedCourseHomeworks),
    path('loadUserExecution/', views.loadUserExecution),
    path('getCheckedExecutions/', views.getCheckedExecutions),
    path('getExcellentExecutions/<str:homework_id>/', views.getExcellentExecutions),
    path('getExcellentExecutionUserNames/<str:homework_id>/', views.getExcellentExecutionUserNames),
    path('getExecutionsById/<str:homework_id>/', views.getExecutionsById),
    path('getExecutionExcellentById/<str:execution_id>/', views.getExecutionExcellentById),
    path('getUserStarExecutions/<str:user_id>/', views.getUserStarExecutions),
    path('removeStar/', views.removeStar),
    path('getCourseId/<str:homework_id>/', views.getCourseId),
    path('getExecutionById/<str:execution_id>/', views.getExecutionById),
    path('getHomeworks/<str:user_id>/', views.AssignmentAPI.as_view()),
    path('getHomeworkById/', views.AssignmentAPI.as_view()),
    path('fetchCourseHomeworks/', views.AssignmentAPI.as_view()),
    path('fetchFinishHomeworks/', views.AssignmentAPI.as_view()),
    path('getExecutions/', views.ExecutionAPI.as_view()),
    path('getExecution/', views.ExecutionAPI.as_view()),
    path('getExecutionImages/<str:execution_id>/', views.MediaAPI.as_view()),
    path('getStar/', views.StarAPI.as_view()),
    path('setStar/', views.StarAPI.as_view()),
]
