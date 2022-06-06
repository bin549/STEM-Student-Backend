from django.urls import path
from course import views


urlpatterns = [
    path('course/getAll/', views.CourseAPI.as_view()),
    path('course/getRecomendentions/', views.CourseAPI.as_view()),
    path('course/getCount/', views.CourseAPI.as_view()),
    path('course/getByTitle/', views.CourseAPI.as_view()),
    path('course/getByUserId/', views.CourseAPI.as_view()),
    path('genre/getAll/', views.GenreAPI.as_view()),
    path('lecture/updateLastViewedStatus/', views.LectureAPI.as_view()),
    path('lecture/getAll/', views.LectureAPI.as_view()),
    path('lecture/getLastViewed/', views.LectureAPI.as_view()),
    path('lecture/getById/', views.LectureAPI.as_view()),
    path('lecture/getStatuses/', views.ProgressAPI.as_view()),
    path('selection/create/', views.SelectionAPI.as_view()),
    path('selection/get/', views.SelectionAPI.as_view()),
    path('wishlist/create/', views.WishlistAPI.as_view()),
    path('wishlist/delete/', views.WishlistAPI.as_view()),
    path('wishlist/get/', views.WishlistAPI.as_view()),
    path('comment/getAll/', views.CommentAPI.as_view()),
    path('comment/create/', views.CommentAPI.as_view()),
    path('comment/delete/', views.CommentAPI.as_view()),
    path('history/create/', views.HistoryAPI.as_view()),
    path('history/delete/', views.HistoryAPI.as_view()),
    path('history/getAll/', views.HistoryAPI.as_view()),
    path('format/getAll/', views.FormatAPI.as_view()),
    path('progress/get/', views.ProgressAPI.as_view()),
    path('progress/update/', views.ProgressAPI.as_view()),
]
