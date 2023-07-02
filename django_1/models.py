from django.db import models
from django.db.models import Model

from basic_info.base_model import BaseModel


# Create your models here.
class UsernameModel(BaseModel):
    username = models.CharField(max_length=20, unique=True, verbose_name='username1')
    first_name = models.CharField(max_length=18, blank=True, null=True, verbose_name='firstname1')
    last_name = models.CharField(max_length=18, blank=True, null=True, verbose_name='lastname1')
    email = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='email1')
    password = models.CharField(max_length=30, verbose_name='pass1')
    age = models.IntegerField(blank=True, null=True, verbose_name='age1')
    wage = models.IntegerField(blank=True, null=True, verbose_name='wage1')

    class Meta:
        db_table = 't_user'
        verbose_name = 'Usertable'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"THIS IS :{self.username}, ID is :{self.id}"


class EmployeeModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name1')
    age = models.IntegerField(blank=True, null=True, verbose_name='age1')
    wage = models.IntegerField(blank=True, null=True, verbose_name='wage1')
    phone = models.IntegerField(unique=True, blank=True, null=True, verbose_name='phone1')
    email = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='email1')


    """Binding Relative models"""

    dept = models.ForeignKey('DeptModel', null=True, blank=True,related_name='emp_list', on_delete=models.SET_NULL)
    id_numbers = models.OneToOneField('Id_num', null=True, blank=True, on_delete=models.SET_NULL)
    roles = models.ManyToManyField('RoleModel',db_table='t_Ro', blank=True)
    """Database Via third party table"""



    class Meta:
        db_table = 't_Employee'
        verbose_name = 'Employeetable'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"Hi, my name is:{self.name},my ID is:{self.id},my id_numbers is:{self.id_numbers_id}"


class DeptModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name1')
    address = models.CharField(max_length=20, verbose_name='location_dept')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 't_Dept'
        verbose_name = 'Departmentstable'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"This department is {self.name, self.id, self.address, self.parent}"


class Id_num(BaseModel):
    id_number = models.CharField(unique=True, verbose_name='idnumber', max_length=18)

    class Meta:
        db_table = 't_ID'
        verbose_name = 'idnumber'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"This person ID_number is {self.id_number}"


class RoleModel(BaseModel):
    name = models.CharField(unique=True, max_length=20, verbose_name='authority')

    class Meta:
        db_table = 't_auth'
        verbose_name = 'Authority'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"This person is {self.name}"
