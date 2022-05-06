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
    path('addFollow/', views.addFollow),
    path('removeFollow/', views.removeFollow),


    path('getProfile/<str:user_id>/', views.ProfileAPI.as_view()),
    path('getOwner/', views.ProfileAPI.as_view()),
    path('getFollow/', views.FollowAPI.as_view()),
    path('getFollowers/', views.FollowAPI.as_view()),
    path('getFollowings/', views.FollowAPI.as_view()),
    path('getNotes/<str:user_id>/', views.NoteAPI.as_view()),
    path('getNoteById/', views.NoteAPI.as_view()),
    path('createNote/', views.NoteAPI.as_view()),
    path('updateNote/', views.NoteAPI.as_view()),
    path('deleteNote/', views.NoteAPI.as_view()),
    path('createMessage/', views.MessageAPI.as_view()),
    path('getPhotos/', views.PhotoAPI.as_view()),
    path('createPhoto/', views.PhotoAPI.as_view()),
    path('deletePhoto/', views.PhotoAPI.as_view()),
    path('updatePhotoCover/', views.PhotoAPI.as_view()),
    path('getPhoto/', views.PhotoAPI.as_view()),
]
