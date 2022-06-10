from django.db import models
from django.utils import timezone


# Create your models her
class DepartmentModel(models.Model):
    '''Model definition for DepartmentModel.'''

    department_name = models.TextField()
    hod = models.IntegerField(null=True)
    Teacher = models.IntegerField(null=True)
    Courses = models.IntegerField(null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        '''Meta definition for DepartmentModel.'''

        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        '''Unicode representation of DepartmentModel.'''
        return self.department_name
