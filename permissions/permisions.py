from rest_framework.permissions import BasePermission
from courses.models import Course


class IsSubscribed(BasePermission):

  def has_permission(self, request, view):
    course_id = request.parser_context['kwargs'].get('pk') or request.parser_context['kwargs'].get('course_pk')
    course = Course.objects.get(pk=course_id) or Course.objects.get(course_pk=course_id)
    isExist = course in request.user.courses.all()
    return isExist


class IsSubscribedOrIsAdmin(BasePermission):

  def has_permission(self, request, view):
    course_id = request.parser_context['kwargs'].get('pk') or request.parser_context['kwargs'].get('course_pk')
    course = Course.objects.get(pk=course_id)
    isExist = course in request.user.courses.all() or request.user.is_staff
    return isExist