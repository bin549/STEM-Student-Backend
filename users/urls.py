from django.urls import path
from users import views


urlpatterns = [
    path('getUserByUserName/<str:pk>/', views.getUserByUserName),
    path('getUserTypeName/', views.getUserTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('getUserNameById/<str:user_id>/', views.getUserNameById),
    path('getUserById/<str:user_id>/', views.getUserById),
    path('updateUser/', views.updateUser),
    path('getUserTypeById/<str:user_type_id>/', views.getUserTypeById),
    path('createMessage/', views.createMessage),
    path('getInboxReadCount/<str:user_name>/', views.getInboxReadCount),
    path('getInboxUnreadCount/<str:user_name>/', views.getInboxUnreadCount),
    path('getMessages/', views.getMessages),
    path('getMessage/<str:message_id>/', views.getMessage),
    path('SetMessageIsReadStatus/<str:message_id>/', views.SetMessageIsReadStatus),
    path('addFollow/', views.addFollow),
    path('removeFollow/', views.removeFollow),
    path('getFollowersId/<str:user_id>/', views.getFollowersId),
    path('getFollowingsId/<str:user_id>/', views.getFollowingsId),
    path('createNote/', views.createNote),
    path('getProfile/<str:user_id>/', views.ProfileAPI.as_view()),
    path('getFollow/', views.FollowAPI.as_view()),
    path('getNotes/<str:user_id>/', views.NoteAPI.as_view()),
    path('getNoteById/', views.NoteAPI.as_view()),
]
