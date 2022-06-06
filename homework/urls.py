from django.urls import path
from homework import views


urlpatterns = [
    path('homework/getById/', views.AssignmentAPI.as_view()),
    path('homework/getByUserId/', views.AssignmentAPI.as_view()),
    path('homework/getByCourseId/', views.AssignmentAPI.as_view()),
    path('homework/getByFinish/', views.AssignmentAPI.as_view()),
    path('execution/update/', views.ExecutionAPI.as_view()),
    path('execution/getAll/', views.ExecutionAPI.as_view()),
    path('execution/get/', views.ExecutionAPI.as_view()),
    path('media/getByExecutionId/', views.MediaAPI.as_view()),
    path('star/create/', views.StarAPI.as_view()),
    path('star/delete/', views.StarAPI.as_view()),
    path('star/get/', views.StarAPI.as_view()),
    path('star/getAll/', views.StarAPI.as_view()),
    path('activityLog/create/', views.LogAPI.as_view()),
]
