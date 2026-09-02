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

def health_check(request):
    """Une vue simple qui renvoie un statut de succès."""
    return JsonResponse({"status": "ok", "message": "API is healthy"})

def trigger_error(request):
    """Une vue conçue pour créer une erreur 500."""
    # Cette ligne va inévitablement provoquer une erreur
    division_by_zero = 1 / 0
    return JsonResponse({"this": "will never be returned"})