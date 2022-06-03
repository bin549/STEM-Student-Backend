from django.urls import path
from course import views


urlpatterns = [
    path('getAllVisibleCourse/', views.AllVisibleCourse.as_view()),
    path('courses/<slug:genre_slug>/', views.GenreDetail.as_view()),
    path('getCourseVisibleStatus/', views.getCourseVisibleStatus),
    path('getCourseOwner/', views.getCourseOwner),
    path('getCourseGenre/<str:genre_id>/', views.getCourseGenre),
    path('getLectureFormat/<str:format_id>/', views.getLectureFormat),
    path('loadCurrentSelectCourseTitle/<str:course_id>/', views.loadCurrentSelectCourseTitle),

    path('getCourses/', views.CourseAPI.as_view()),
    path('getCourse/<str:course_name>/', views.CourseAPI.as_view()),
    path('getRecomendedCourses/', views.CourseAPI.as_view()),
    path('getCoursesCount/', views.CourseAPI.as_view()),
    path('getGenres/', views.GenreAPI.as_view()),
    path('getLectures/', views.LectureAPI.as_view()),
    path('getLastViewedLecture/', views.LectureAPI.as_view()),
    path('getLectureById/', views.LectureAPI.as_view()),
    path('updateLastViewedStatus/', views.LectureAPI.as_view()),
    path('getSelection/', views.SelectionAPI.as_view()),
    path('createSelection/', views.SelectionAPI.as_view()),
    path('createWishlist/', views.WishlistAPI.as_view()),
    path('deleteWishlist/', views.WishlistAPI.as_view()),
    path('getWishlist/', views.WishlistAPI.as_view()),
    path('getWishlistCourses/', views.WishlistAPI.as_view()),
    path('getComments/', views.CommentAPI.as_view()),
    path('getCommentsByUserId/', views.CommentAPI.as_view()),
    path('createComment/', views.CommentAPI.as_view()),
    path('deleteComment/', views.CommentAPI.as_view()),
    path('createHistory/', views.HistoryAPI.as_view()),
    path('getHistories/', views.HistoryAPI.as_view()),
    path('deleteHistory/', views.HistoryAPI.as_view()),
    path('getFormats/', views.FormatAPI.as_view()),
    path('getProgress/', views.ProgressAPI.as_view()),
    path('updateProgress/', views.ProgressAPI.as_view()),
    path('getLecturesStatus/', views.ProgressAPI.as_view()),
]
