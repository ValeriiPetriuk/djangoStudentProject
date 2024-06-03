from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    class RolesChoice(models.TextChoices):
        STUDENT = "Student", "Student"
        TEACHER = "Teacher", "Teacher"

    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, unique=True)
    groups = models.ForeignKey("Group", related_name='groups', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(choices=RolesChoice.choices, default=RolesChoice.STUDENT, max_length=10)
    photo = models.ImageField(upload_to='user/photo', blank=True, null=True)


