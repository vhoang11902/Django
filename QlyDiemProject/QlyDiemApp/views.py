from django.shortcuts import render
from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Course, Department, User, MainScore
from .serializers import CourseSerializer, DepartmentSerializer, UserSerializer, MainScoreSerializer
from django.http import HttpResponse
# Create your views here.


from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Allow GET requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is a teacher
        return request.user.groups.filter(name='Teacher').exists()



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter(active=True)
    serializer_class = DepartmentSerializer
    # permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]


class MainScoreViewSet(viewsets.ModelViewSet):
    queryset = MainScore.objects.filter(active=True)
    serializer_class = MainScoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class =UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='current-user', url_name='current-user', detail=False)
    def current_user(self, request):
        user_data = UserSerializer(request.user).data
        user_group = UserSerializer.getUserGroup(request.user)  # Hàm get_user_group được định nghĩa ở phần trước
        user_data['group'] = user_group  # Thêm thông tin nhóm vào dữ liệu người dùng
        return Response(user_data)

    def retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)
# def index(request):
#     return render(request, template_name='index.html')