from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import railway_test

from api import views

router = DefaultRouter()

router.register('categories', views.CategoryViewSet)
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test-railway/', views.railway_test, name='railway_test'),
]