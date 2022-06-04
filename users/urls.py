from django.urls import path
from users import views


urlpatterns = [
    path('getUserByUserName/<str:pk>/', views.getUserByUserName),
    path('getUserTypeName/', views.getUserTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('getUserNameById/<str:user_id>/', views.getUserNameById),
    path('updateUser/', views.updateUser),
    path('getUserTypeById/<str:user_type_id>/', views.getUserTypeById),
    path('getInboxReadCount/<str:user_name>/', views.getInboxReadCount),
    path('getInboxUnreadCount/<str:user_name>/', views.getInboxUnreadCount),
    path('getMessages/', views.getMessages),
    path('getMessage/<str:message_id>/', views.getMessage),
    path('SetMessageIsReadStatus/<str:message_id>/', views.SetMessageIsReadStatus),


    path('message/create/', views.MessageAPI.as_view()),
    path('registerUser/', views.ProfileAPI.as_view()),
    path('Profile/get/', views.ProfileAPI.as_view()),
    path('getCourseOwner/', views.ProfileAPI.as_view()),
    path('getOwner/', views.ProfileAPI.as_view()),
    path('getFollow/', views.FollowAPI.as_view()),
    path('getFollowers/', views.FollowAPI.as_view()),
    path('getFollowings/', views.FollowAPI.as_view()),
    path('createFollow/', views.FollowAPI.as_view()),
    path('deleteFollow/', views.FollowAPI.as_view()),
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
