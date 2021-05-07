from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from permissions.permisions import IsSubscribed, IsSubscribedOrIsAdmin
from .serialaizers import TheorySerializer
from theories.models import Theory
from theories.selectors import get_theories_list, get_theory_object

class TheoryViewSet(viewsets.ModelViewSet):
  serializer_class = TheorySerializer
  queryset = Theory.objects.all()
  def get_permissions(self):
    if self.action in ('retrieve', 'list'):
        permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]
    else:
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]
  
  def get_queryset(self):
    if self.action in ('retrieve', 'update', 'destroy', 'partial_update'):
      return Theory.objects.filter(lesson=self.kwargs['lesson_pk'], pk=self.kwargs['pk'])
    return get_theories_list(self)
      

