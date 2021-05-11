from django.db import models


# Create your models here.
class Recruitment(models.Model):
    id = models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=150)
    blood_group = models.CharField(max_length=3)
    section = models.CharField(max_length=2)

    class Meta:
        db_table = 'Recruitment'


class Apply(models.Model):
    id = models.OneToOneField(Recruitment, on_delete=models.CASCADE)
    extra = models.CharField(max_length=500)
    interest = models.CharField(max_length=500)
    why = models.CharField(max_length=500)

    class Meta:
        db_table = 'Apply'
