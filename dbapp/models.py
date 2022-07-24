from django.db import models

# Create your models here.

# Enumerations
class VacName(models.IntegerChoices):
    NONE = 0
    COVAXIN = 1
    COVISHIELD = 2

class GovtID(models.IntegerChoices):
    AADHAAR = 1
    PASSPORT = 2
    BIRTH_CERT = 3

class Student(models.Model):
    sid = models.CharField(max_length=10, primary_key=True)
    sfname = models.CharField(max_length=20)
    slname = models.CharField(max_length=20)
    dob = models.DateField()
    gidtype = models.IntegerField(choices=GovtID.choices, default=1)
    gidno = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    vaccine = models.IntegerField(choices=VacName.choices, default=0)

    def __str__(self):
        return self.sid


class VacDoseStatus(models.Model):
    sid = models.ForeignKey('Student', on_delete=models.CASCADE, related_name="vac_details")
    vacName = models.IntegerField(choices=VacName.choices, default=0)
    vacDateD1 = models.DateField()
    vacDateD2 = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.sid)




