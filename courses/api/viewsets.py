from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from permissions.permisions import IsSubscribed, IsSubscribedOrIsAdmin
from courses.models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from courses.selectors import get_courses_list, get_course_detail, get_lessons_list, get_lesson_detail


class CourseViewSet(viewsets.ModelViewSet):
  serializer_class = CourseSerializer
  queryset = Course.objects.all()

  @action(detail=True,
          methods=['post'],
          permission_classes=[IsAuthenticated],
          name='subscribe')
  def subscribe(self, request, *args, **kwargs):
    user = self.request.user
    course = get_course_detail(self)
    if(course in user.courses.all()):
      return Response({'status': 'user is already subscribed'}, status=status.HTTP_208_ALREADY_REPORTED)
    if(not course.available):
      return Response({'status': 'course is not available (course was started)'}, status=status.HTTP_403_FORBIDDEN)
    user.courses.add(course)
    user.save()
    return Response({'status': 'subscribed'}, status=status.HTTP_200_OK)


  @action(detail=True,
          methods=['post'],
          permission_classes=[IsAuthenticated, IsSubscribed],
          name='unsubscribe')
  def unsubscribe(self, request, *args, **kwargs):
    print(request)
    user = self.request.user
    course = get_course_detail(self)
    if(not course.available):
      return Response({'status': 'you can not unsubscribe (course was started)'}, status=status.HTTP_403_FORBIDDEN)
    user.courses.remove(course)
    user.save()
    return Response({'status': 'unsubscriped'}, status=status.HTTP_200_OK)

class LessonViewSet(viewsets.ModelViewSet):
  serializer_class = LessonSerializer
  def get_permissions(self):
    if self.action in ('retrieve', 'list'):
        permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]
    else:
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]

  def get_queryset(self):
    if self.action in ('retrieve', 'destroy', 'update', 'partial_update'):
      return Lesson.objects.filter(pk=self.kwargs['pk'], course=self.kwargs['course_pk'])
    return get_lessons_list(self)