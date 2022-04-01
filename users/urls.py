from django.urls import path
from users import views


urlpatterns = [
    path('getAllUsers/', views.AllUsers.as_view()),
    path('getUserByUserName/<str:pk>/', views.getUserByUserName),
    path('getUserTypeName/', views.getUserTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('addUser/', views.addUser),
    path('createMessage/', views.createMessage),
    path('getInboxReadCount/<str:user_name>/', views.getInboxReadCount),
    path('getInboxUnreadCount/<str:user_name>/', views.getInboxUnreadCount),
    path('getMessages/', views.getMessages),
    path('getMessage/<str:message_id>/', views.getMessage),
    path('SetMessageIsReadStatus/<str:message_id>/', views.SetMessageIsReadStatus),
    path('deleteMessage/<str:message_id>/', views.deleteMessage),
    path('getUserNameById/<str:user_id>/', views.getUserNameById),
    path('getUserById/<str:user_id>/', views.getUserById),
    path('updateUser/', views.updateUser),
    path('getUserInfoById/<str:user_id>/', views.getUserInfoById),
    path('getFollowStatus/', views.getFollowStatus),
    path('addFollow/', views.addFollow),
    path('removeFollow/', views.removeFollow),
    path('getFollowersId/<str:user_id>/', views.getFollowersId),
    path('getFollowingsId/<str:user_id>/', views.getFollowingsId),
    path('getUserTypeById/<str:user_type_id>/', views.getUserTypeById),
    path('getNotes/<str:user_id>/', views.getNotes),
    path('createNote/', views.createNote),
    path('getNoteById/<str:note_id>/', views.getNoteById),
]
