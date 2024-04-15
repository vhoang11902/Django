from rest_framework.serializers import ModelSerializer
from .models import Course, Department, User, MainScore
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class MainScoreSerializer(ModelSerializer):
    class Meta:
        model = MainScore
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'username': {
                'write_only': True
            }
        }

    def getUserGroup(user):
        groups = user.groups.all()
        group_names = [group.name for group in groups]

        return group_names

    def validate_email(self, value):
        if not value.endswith('@ou.edu.vn'):
            raise ValidationError("Email must end with '@ou.edu.vn'")
        return value


    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data['password'])
        user.save()

        student_group = Group.objects.get(name='student')
        user.groups.add(student_group)
        return user
