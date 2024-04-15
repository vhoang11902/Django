from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('department', views.DepartmentViewSet)
router.register('courses', views.CourseViewSet)
router.register('users', views.UserViewSet, basename='users')
router.register('mainScore', views.MainScoreViewSet)

urlpatterns = [
    path('', include(router.urls))
]