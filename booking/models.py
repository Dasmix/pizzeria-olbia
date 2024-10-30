from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

TIME_CHOICES = (
    ('5:30 PM', '5:30 PM'),
    ('6:00 PM', '6:00 PM'),
    ('6:30 PM', '6:30 PM'),
    ('7:00 PM', '7:00 PM'),
    ('7:30 PM', '7:30 PM'),
    ('8:00 PM', '8:00 PM'),
    ('8:30 PM', '8:30 PM'),
    ('9:00 PM', '9:00 PM'),
    ('9:30 PM', '9:30 PM'),
    ('10:00 PM', '10:00 PM')
)

GUEST_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Reservation (models.Model):
    guest = models.CharField(max_length=10, choices=GUEST_CHOICES)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
