from django.urls import path
from course import views


urlpatterns = [
    path('getAllCourse/', views.AllCourse.as_view()),
    path('getAllVisibleCourse/', views.AllVisibleCourse.as_view()),
    path('getRecomendedCourse/', views.getRecomendedCourse),
    path('getAllGenres/', views.AllGenre.as_view()),
    path('getAllSelection/', views.AllSelection.as_view()),
    path('getAllCollection/', views.AllCollection.as_view()),
    path('course/<str:course_name>/', views.getCourseDetail),
    path('courses/<slug:genre_slug>/', views.GenreDetail.as_view()),
    path('getUserSelection/<str:user_id>/', views.getUserSelection),
    path('getCourseLectures/<str:course_id>/', views.getCourseLectures),
    path('getUserWishlist/<str:user_id>/', views.getUserWishlist),
    path('getOwnerCourse/<str:user_id>/', views.getOwnerCourse),
    path('course_student/<slug:course_slug>/', views.SelectionUser.as_view()),
    path('createCourse/', views.createCourse),
    path('updateCourse/<str:pk>/', views.updateCourse),
    path('deleteCourse/', views.deleteCourse),
    path('getSerialNumber/', views.getSerialNumber),
    path('registerCourse/', views.registerCourse),
    path('getCourseStatus/', views.getCourseStatus),
    path('getWishlistStatus/', views.getWishlistStatus),
    path('addWishlist/', views.addWishlist),
    path('removeWishlist/', views.removeWishlist),
    path('getCourseVisibleStatus/', views.getCourseVisibleStatus),
    path('setCourseVisible/', views.setCourseVisible),
    path('addCourseStudent/', views.addCourseStudent),
    path('deleteCourseStudent/', views.deleteCourseStudent),
    path('addCourseLecture/', views.addCourseLecture),
    path('getCourseByTypeAndPage/', views.getCourseByTypeAndPage),
    path('getCoursesCount/', views.getCoursesCount),
    path('getUserCoursesByTypeAndPage/', views.getUserCoursesByTypeAndPage),
    path('getMyCoursesCount/', views.getMyCoursesCount),
    path('savefile/', views.savefile),
    path('getCourseOwner/<str:course_id>/', views.getCourseOwner),
    path('getCourse/<str:course_id>/', views.getCourse),
    path('getCourseGenre/<str:genre_id>/', views.getCourseGenre),
    path('deleteLecture/', views.deleteLecture),
    path('setPreviewLecture/', views.setPreviewLecture),
    path('getPreviewLectureByCourseId/<str:course_id>/', views.getPreviewLectureByCourseId),
    path('getCourseLecture/', views.getCourseLecture),
    path('getLectureFormat/<str:format_id>/', views.getLectureFormat),
]
