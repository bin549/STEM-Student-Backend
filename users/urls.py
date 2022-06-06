from django.urls import path
from users import views


urlpatterns = [
    path('user/create/', views.UserAPI.as_view()),
    path('follow/create/', views.FollowAPI.as_view()),
    path('follow/delete/', views.FollowAPI.as_view()),
    path('follow/getFollowers/', views.FollowAPI.as_view()),
    path('follow/getFollowings/', views.FollowAPI.as_view()),
    path('follow/get/', views.FollowAPI.as_view()),
    path('message/create/', views.MessageAPI.as_view()),
    path('profile/getByUsername/', views.ProfileAPI.as_view()),
    path('profile/get/', views.ProfileAPI.as_view()),
    path('note/create/', views.NoteAPI.as_view()),
    path('note/delete/', views.NoteAPI.as_view()),
    path('note/update/', views.NoteAPI.as_view()),
    path('note/getAll/', views.NoteAPI.as_view()),
    path('note/getById/', views.NoteAPI.as_view()),
    path('photo/getAll/', views.PhotoAPI.as_view()),
    path('photo/getById/', views.PhotoAPI.as_view()),
    path('photo/create/', views.PhotoAPI.as_view()),
    path('photo/delete/', views.PhotoAPI.as_view()),
    path('photo/updateCover/', views.PhotoAPI.as_view()),
]
