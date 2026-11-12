from django.db import models


class Pet(models.Model):
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]
    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20, choices=PET_TYPES)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDERS, default='Unknown')
    color = models.CharField(max_length=50, blank=True)
    owner_name = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=30)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name