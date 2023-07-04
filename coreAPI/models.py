from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import FieldError
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from basic_info.base_model import BaseModel
from django.core.exceptions import FieldDoesNotExist


class JobChoices(models.TextChoices):

    MR = "Manager"
    CE = "Co_Employee"
    PR = "President"

class StudentModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='Name')
    entry_data = models.DateTimeField(blank=True, null=True,default=datetime,verbose_name='Entry_data')
    age = models.IntegerField(blank=True, null=True, verbose_name='Age')
    job_title = models.TextField(max_length=11,choices=JobChoices.choices,  verbose_name='Job_title')
    wage = models.IntegerField(blank=True, null=True, verbose_name='Wage')
    bonu = models.IntegerField(unique=True, blank=True, null=True, verbose_name='Bonus')
    email = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='E-mail1')

    dept = models.ForeignKey('DeptModel', null=True, blank=True, related_name='Stu_list', on_delete=models.SET_NULL)
    class Meta:
        db_table = 't_Student'
        verbose_name = 'Student_table'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"Hi, my name is:{self.name},my ID is:{self.id}"

class DeptModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='Det_name')
    address = models.CharField(max_length=20, verbose_name='Location_dept')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 't_Dept_CORE'
        verbose_name = 'Departments_table2'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"This department is {self.name, self.id, self.address, self.parent}"



class UserloginModel(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='username1')
    email = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='email1')
    password = models.CharField(max_length=100, verbose_name='pass')
    phone = models.IntegerField(verbose_name='phone_num')





    groups = models.ManyToManyField(Group, related_name='userlogins')
    user_permissions = models.ManyToManyField(Permission, related_name='userlogins')

    class Meta:
        db_table = 't_userlogin'
        verbose_name = 'User_table'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"THIS IS :{self.username}, ID is :{self.id}"