from django.urls import path, include
from .viewsets import CourseViewSet, LessonViewSet
from tests.api.viewsets import TestViewSet
from theories.api.viewsets import TheoryViewSet
from homeworks.api.viewsets import HomeworkViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet, basename="courses")

course_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
course_router.register(r'lessons', LessonViewSet, basename="lessons")

test_router = routers.NestedSimpleRouter(course_router, r'lessons', lookup='lesson')
test_router.register(r'tests', TestViewSet, basename='tests')

theory_router = routers.NestedSimpleRouter(course_router, r'lessons', lookup='lesson')
theory_router.register(r'theories', TheoryViewSet, basename='theories')

homework_router = routers.NestedSimpleRouter(course_router, r'lessons', lookup='lesson')
homework_router.register(r'homeworks', HomeworkViewSet, basename='homeworks')

urlpatterns = [
  path('', include(router.urls)),
  path('', include(course_router.urls)),
  path('', include(test_router.urls)),
  path('', include(theory_router.urls)),
  path('', include(homework_router.urls)),
]
