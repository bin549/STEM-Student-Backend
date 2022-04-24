from django.urls import path
from course import views


urlpatterns = [
    path('getAllVisibleCourse/', views.AllVisibleCourse.as_view()),
    path('getAllCollection/', views.AllCollection.as_view()),
    path('courses/<slug:genre_slug>/', views.GenreDetail.as_view()),
    path('getAllSelection/', views.AllSelection.as_view()),
    path('getUserWishlist/<str:user_id>/', views.getUserWishlist),
    path('getCourseVisibleStatus/', views.getCourseVisibleStatus),
    path('addCourseStudent/', views.addCourseStudent),
    path('getCourseOwner/<str:course_id>/', views.getCourseOwner),
    path('getCourseGenre/<str:genre_id>/', views.getCourseGenre),
    path('getLectureFormat/<str:format_id>/', views.getLectureFormat),
    path('loadCurrentSelectCourseTitle/<str:course_id>/', views.loadCurrentSelectCourseTitle),

    path('getCourses/', views.CourseAPI.as_view()),
    path('getCourse/<str:course_name>/', views.CourseAPI.as_view()),
    path('getRecomendedCourse/', views.CourseAPI.as_view()),
    path('getCoursesCount/', views.CourseAPI.as_view()),
    path('getGenres/', views.GenreAPI.as_view()),
    path('getPreviewLecture/', views.LectureAPI.as_view()),
    path('getLectures/<str:course_id>/', views.LectureAPI.as_view()),
    path('getLectureById/', views.LectureAPI.as_view()),
    path('getSelection/', views.SelectionAPI.as_view()),
    path('createSelection/', views.SelectionAPI.as_view()),
    path('createWishlist/', views.WishlistAPI.as_view()),
    path('deleteWishlist/', views.WishlistAPI.as_view()),
    path('getWishlist/', views.WishlistAPI.as_view()),
    path('getComments/<str:lecture_id>/', views.CommentAPI.as_view()),
    path('getCommentsByUserId/', views.CommentAPI.as_view()),
    path('createComment/', views.CommentAPI.as_view()),
    path('deleteComment/', views.CommentAPI.as_view()),
]
