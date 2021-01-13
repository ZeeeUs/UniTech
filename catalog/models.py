from django.db import models
from django.urls import reverse

import uuid

from django.utils import timezone


class Technik(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Territory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OrderDuration(models.Model):
    worktime = models.CharField(max_length=255)

    def __str__(self):
        return self.worktime


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    technik = models.ForeignKey('Technik', on_delete=models.CASCADE)
    customer = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=255)
    territory = models.ForeignKey('Territory', on_delete=models.SET_NULL, null=True)
    duration = models.ForeignKey('OrderDuration', on_delete=models.PROTECT)
    note = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False, default=timezone.now)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}.{1}'.format(self.id, self.technik.name)
