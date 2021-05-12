from django.db import models


# Create your models here.
class Recruitment(models.Model):

    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)
    reg = models.CharField(primary_key=True, max_length=15, null=False)
    phone = models.CharField(max_length=15, null=True)
    blood = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=150, null=True)


    class Meta:
        db_table = 'Recruitment'


class Apply(models.Model):
    reg = models.CharField(max_length=15)
    extra = models.CharField(max_length=500)
    interest = models.CharField(max_length=500)
    why = models.CharField(max_length=500)

    class Meta:
        db_table = 'Apply'
