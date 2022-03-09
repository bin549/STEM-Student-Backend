from django.urls import path
from users import views


urlpatterns = [
    path('getAllUsers/', views.AllUsers.as_view()),
    path('getUserInfo/<str:pk>/', views.getUserInfo),
    path('getUserTypeName/', views.getUserTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('getUsersByTypeName/<str:type_name>/', views.getUsersByTypeName),
    path('addUser/', views.addUser),
    path('createMessage/', views.createMessage),
    path('getInboxUnreadCount/', views.getInboxUnreadCount),
    path('getInboxReadCount/', views.getInboxReadCount),
    path('getMessages/', views.getMessages),
    path('getMessage/<str:message_id>/', views.getMessage),
    path('SetMessageIsReadStatus/<str:message_id>/', views.SetMessageIsReadStatus),
    path('deleteMessage/<str:message_id>/', views.deleteMessage),
    path('getUserNameById/<str:user_id>/', views.getUserNameById),
    path('getUserById/<str:user_id>/', views.getUserById),
    path('updateUser/', views.updateUser),
]
