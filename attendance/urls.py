from django.urls import path, include, re_path
from attendance.views import SemesterApiView, CourseApiView, LecturerApiView, StudentApiView, CollegeDayApiView, AttendanceApiView, ClassApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'semesters', SemesterApiView, basename='semester')
router.register(r'courses', CourseApiView, basename='course')
router.register(r'lecturers', LecturerApiView, basename='lecturer')
router.register(r'students', StudentApiView, basename='student')
router.register(r'collegedays', CollegeDayApiView, basename='collegeday')
router.register(r'attendances', AttendanceApiView, basename='attendance')
router.register(r'classes', ClassApiView, basename='class')
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += router.urls
#
# urlpatterns = [
#     path("semester", SemesterApiView.as_view({
#         'get': 'get',
#         'post': 'post',
#     })),
#     re_path("^semester/(?P<pk>\d+)$", SemesterApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
#     path("course", CourseApiView.as_view({
#         'get': 'get',
#         'post': 'post'
#     })),
#     re_path("^course/(?P<pk>\d+)$", CourseApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
#     path("lecturer", LecturerApiView.as_view({
#         'get': 'get',
#         'post': 'post'
#     })),
#     re_path("^lecturer/(?P<pk>\d+)$", LecturerApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
#     path("student", StudentApiView.as_view({
#         'get': 'get',
#         'post': 'post'
#     })),
#     re_path("^student/(?P<pk>\d+)$", StudentApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
#     path("collegeday", CollegeDayApiView.as_view({
#         'get': 'get',
#         'post': 'post'
#     })),
#     re_path("^collegeday/(?P<pk>\d+)$", CollegeDayApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
#     path("attendance", AttendanceApiView.as_view({
#         'get': 'get',
#         'post': 'post'
#     })),
#     re_path("^attendance/(?P<pk>\d+)$", AttendanceApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
#     path("class", ClassApiView.as_view({
#         'get': 'get',
#         'post': 'post'
#     })),
#     re_path("^class/(?P<pk>\d+)$", ClassApiView.as_view({
#         'get': 'getone',
#         'patch': 'update',
#         'delete': 'delete'
#     })),
# ]

