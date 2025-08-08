from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_id>/projects/', ProjectViewSet.as_view({'post': 'create'}), name='client-projects'),
    path('projects/', ProjectViewSet.as_view({'get': 'list'}), name='user-projects'),
]
