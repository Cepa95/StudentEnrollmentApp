from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from enum import Enum

# Create your models here.

class Korisnici(AbstractUser):
    class RoleChoices(Enum):
        ADMINISTRATOR = 'administrator'
        PROFESOR = 'profesor'
        STUDENT = 'student'

    class StatusChoices(Enum):
        NONE = 'none'
        REDOVAN = 'redovan'
        IZVANREDAN = 'izvanredan'

    role = models.CharField(max_length=20, choices=[(role.value, role.name) for role in RoleChoices])
    status = models.CharField(max_length=20, choices=[(status.value, status.name) for status in StatusChoices])

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='korisnici_set'  # Specify a unique related_name
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='korisnici_set'  # Specify a unique related_name
    )

    @classmethod
    def get_students(cls):
        return cls.objects.filter(role=cls.RoleChoices.STUDENT.value)



class Predmeti(models.Model):
    IZBORNI = (('da', 'da'), ('ne', 'ne'))
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=10)
    program = models.TextField(max_length=50,null=False)
    ects = models.IntegerField(null=False)
    sem_red = models.IntegerField(null=False)
    sem_izv = models.IntegerField(null=False)
    izborni = models.CharField(max_length=10, choices=IZBORNI)
    nositelj = models.ForeignKey(Korisnici, on_delete=models.SET_NULL, null=True, default=None)