from django.urls import path, include
from rest_framework.routers import DefaultRouter
from roles import views

router = DefaultRouter()
router.register('roles', views.RoleViewSet)

app_name = 'roles'

urlpatterns = [
    path('', include(router.urls))
]