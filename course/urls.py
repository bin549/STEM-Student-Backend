from django.urls import path
from course import views


urlpatterns = [
    path('getAllVisibleCourse/', views.AllVisibleCourse.as_view()),
    path('getRecomendedCourse/', views.getRecomendedCourse),
    path('getAllCollection/', views.AllCollection.as_view()),
    path('getUserSelection/<str:user_id>/', views.getUserSelection),
    path('getCourseLectures/<str:course_id>/', views.getCourseLectures),
    path('course/<str:course_name>/', views.getCourseDetail),
    path('courses/<slug:genre_slug>/', views.GenreDetail.as_view()),
    path('registerCourse/', views.registerCourse),
    path('getCourseStatus/', views.getCourseStatus),
    path('getAllGenres/', views.AllGenre.as_view()),
    path('getAllSelection/', views.AllSelection.as_view()),
    path('getUserWishlist/<str:user_id>/', views.getUserWishlist),
    path('getWishlistStatus/', views.getWishlistStatus),
    path('addWishlist/', views.addWishlist),
    path('removeWishlist/', views.removeWishlist),
    path('getCourseVisibleStatus/', views.getCourseVisibleStatus),
    path('addCourseStudent/', views.addCourseStudent),
    path('getCourseByTypeAndPage/', views.getCourseByTypeAndPage),
    path('getCoursesCount/', views.getCoursesCount),
    path('getUserCoursesByTypeAndPage/', views.getUserCoursesByTypeAndPage),
    path('getMyCoursesCount/', views.getMyCoursesCount),
    path('getCourseOwner/<str:course_id>/', views.getCourseOwner),
    path('getCourse/<str:course_id>/', views.getCourse),
    path('getCourseGenre/<str:genre_id>/', views.getCourseGenre),
    path('getCourseLecture/', views.getCourseLecture),
    path('getLectureFormat/<str:format_id>/', views.getLectureFormat),
    path('loadCurrentSelectCourseTitle/<str:course_id>/', views.loadCurrentSelectCourseTitle),
    path('createLectureComment/', views.createLectureComment),
    path('getLectureComments/<str:lecture_id>/', views.getLectureComments),
    path('getOwnerByCourseName/<str:course_name>/', views.getOwnerByCourseName),
    path('getLectureCommentsByUserId/<str:user_id>/', views.getLectureCommentsByUserId),
    path('getLectureById/<str:lecture_id>/', views.getLectureById),
    path('deleteCommentById/<str:comment_id>/', views.deleteCommentById),
    path('getPreviewLecture/', views.LectureAPI.as_view()),
]
