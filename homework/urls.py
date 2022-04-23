from django.urls import path
from homework import views


urlpatterns = [
    path('deleteHomework/', views.deleteHomework),
    path('getAllHomework/', views.AllHomework.as_view()),
    path('loadHomeworks/', views.loadHomeworks),
    path('loadCourseAllHomeworks/', views.loadCourseAllHomeworks),
    path('getHomeworks/<str:user_id>/', views.getHomeworks),
    path('getUnfinishHomework/<str:user_id>/', views.getUnfinishHomework),
    path('getHomeworkById/<str:homework_id>/', views.getHomeworkById),
    path('uploadHomework/', views.uploadHomework),
    path('loadCourseHomeworks/', views.loadCourseHomeworks),
    path('getHomeworkId/<str:execution_id>/', views.getHomeworkId),
    path('loadCourseUnfinishHomeworks/', views.loadCourseUnfinishHomeworks),
    path('loadCourseFinishHomeworks/', views.loadCourseFinishHomeworks),
    path('getSelectedCourseHomeworks/<str:course_id>/', views.getSelectedCourseHomeworks),
    path('loadExecution/', views.loadExecution),
    path('loadUserExecution/', views.loadUserExecution),
    path('getExecutionImages/<str:execution_id>/', views.getExecutionImages),
    path('getCheckedExecutions/', views.getCheckedExecutions),
    path('loadExcellentExecutions/', views.loadExcellentExecutions),
    path('getExcellentExecutions/<str:homework_id>/', views.getExcellentExecutions),
    path('getExcellentExecutionUserNames/<str:homework_id>/', views.getExcellentExecutionUserNames),
    path('getExecutionsById/<str:homework_id>/', views.getExecutionsById),
    path('getExecutionExcellentById/<str:execution_id>/', views.getExecutionExcellentById),
    path('getStarStatus/', views.getStarStatus),
    path('changeStarStatus/', views.changeStarStatus),
    path('getUserStarExecutions/<str:user_id>/', views.getUserStarExecutions),
    path('removeStar/', views.removeStar),
    path('getCourseId/<str:homework_id>/', views.getCourseId),
    path('getExecutionById/<str:execution_id>/', views.getExecutionById),
]
