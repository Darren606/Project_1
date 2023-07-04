from django.db import models

from basic_info.base_model import BaseModel



class EmployeeModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name1')
    age = models.IntegerField(blank=True, null=True, verbose_name='age1')
    wage = models.IntegerField(blank=True, null=True, verbose_name='wage1')
    phone = models.IntegerField(unique=True, blank=True, null=True, verbose_name='phone1')
    email = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='email1')

    class Meta:
        db_table = 't_rest_Employee'
        verbose_name = 'Employeetable'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"Hi, my name is:{self.name},my ID is:{self.id}"
        

class PersonModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name1')
    age = models.IntegerField(blank=True, null=True, verbose_name='age1')
    wage = models.IntegerField(blank=True, null=True, verbose_name='wage1')
    phone = models.IntegerField(unique=True, blank=True, null=True, verbose_name='phone1')
    email = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='email1')

    class Meta:
        db_table = 't_person'
        verbose_name = 'persontable'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"Hi, my name is:{self.name},my ID is:{self.id}"
