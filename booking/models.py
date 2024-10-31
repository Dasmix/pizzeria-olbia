from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

TIME_CHOICES = (
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00')
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
