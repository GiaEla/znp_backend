from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Event(models.Model):
    name = models.CharField('Dogodek', max_length=50, blank=False, null=False)
    short_description = models.CharField('Kratek opis', max_length=50, blank=False, null=False)
    description = models.CharField('Opis', max_length=700, blank=False, null=False)
    start_date = models.DateField('Pričetek', blank=True, null=True)
    end_date = models.DateField('Zaključek', blank=True, null=True)
    img = models.ImageField('Slika')
    registrations = JSONField('Prijave', blank=True, null=True)
