# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal

# Create your models here.
class City(models.Model):

    class Meta:
        verbose_name_plural='cities'

    city_name=models.CharField(max_length=50,default='null')
    airport_code=models.CharField(max_length=50,default='null')
    #flight=models.ManyToManyField(Flight)

    def __str__(self):
        return str(self.city_name)


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airline_name = models.CharField(max_length=50,default='null')
    airline_id = models.CharField(max_length=50,default='null')
    source=models.ForeignKey(City, null=True, related_name='src')
    destination=models.ForeignKey(City, null=True, related_name='dest')
    departure_date = models.DateTimeField(null=True)
    total_seats = models.IntegerField()
    #available_seats=models.IntegerField()

    def __str__(self):
        return str(self.flight_id)




class User(models.Model):
    name=models.CharField(max_length=70,default='null')
    age =   models.IntegerField()
    passport_id=models.CharField(max_length=70,default='null')
    email_id=models.EmailField(max_length=55,primary_key=True)    ###userid
    #flight=models.ForeignKey(Flight)

    def __str__(self):
        return str(self.name)
class TicketDetails(models.Model):
    email_id = models.EmailField(max_length=55,null=True)
    person_name=models.CharField(max_length=70,null=True)
    ticket_id =models.AutoField(primary_key=True)
    source=models.CharField(max_length=70,default='null')
    destination=models.CharField(max_length=70,default='null')
    airline_name=models.CharField(max_length=70,default='null')
    airline_id=models.CharField(max_length=70,default='null')
    departure_date=models.DateTimeField(null=True)
    seats=models.IntegerField()
