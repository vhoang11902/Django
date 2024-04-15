from django.contrib import admin
from .models import Course,Department,Semester, User, MainScore
# Register your models here.

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(User)
admin.site.register(MainScore)


