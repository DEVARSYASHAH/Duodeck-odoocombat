from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Language'
    
class Student(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, verbose_name = 'Language')
    student_id=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='User_id')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        last_4_digits=self.student_id.username[-4:]
        return "{}_{}-{}".format(self.first_name,last_4_digits,self.department)
    

    