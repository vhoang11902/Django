from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)


class Department(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class Semester(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    id = models.CharField(primary_key=True, max_length=200, null=False, unique=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=False, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name


class MainScore(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    midtermScore = models.FloatField(null=True, blank=True)
    midtermPercen = models.FloatField(null=True, blank=True)
    endtermScore = models.FloatField(null=True, blank=True)
    endtermPercen = models.FloatField(null=True, blank=True)
    overallScore = models.FloatField(null=True, blank=True)
    result = models.CharField(max_length=100, null=True)
    locked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Score(BaseModel):
    mainScore = models.ForeignKey(MainScore, on_delete=models.CASCADE)
    score = models.FloatField()
    scorePercen = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

