from django.urls import path, include
from rest_framework_nested import routers

from .viewsets import TestViewSet, QuestionViewSet, AnswerOptionViewSet, UserTestViewSet, UserTestAnswerOptionViewSet
from courses.viewsets import LessonViewSet

lesson_router = routers.SimpleRouter()
lesson_router.register(r'lessons', LessonViewSet)

test_router = routers.NestedSimpleRouter(lesson_router, r'lessons')
test_router.register(r'test', TestViewSet, basename='lessons-test')

question_router = routers.NestedSimpleRouter(test_router, r'test')
question_router.register(r'questions', QuestionViewSet, basename='test-questions')

answer_option_router = routers.NestedSimpleRouter(question_router, r'questions', lookup='question')
answer_option_router.register(r'answer_options', AnswerOptionViewSet, basename='questions-answeroptions')

from .viewsets import TestViewset
urlpatterns = [
    path('', include(lesson_router.urls),
    path('', include(test_router.urls)),
    path('', include(question_router.urls)),
    path('', include(answer_option_router.urls))
]
