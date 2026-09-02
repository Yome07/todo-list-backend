from django.http import JsonResponse
from rest_framework import viewsets

from api.models import Category, Task
from api.serializers import CategorySerializer, TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def railway_test(request):
    """Une vue simple pour valider le déploiement sur Railway."""
    return JsonResponse({"message": "API déployée avec succès sur Railway ! Bravo !"})