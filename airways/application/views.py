# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers


from django.views.generic import View
from datetime import date, datetime
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,QueryDict
from django.core.exceptions import ObjectDoesNotExist
from  application.models import Flight,City,User,TicketDetails
import json


# Create your views here.

class GetFlightsBetweenCities(View):
    def get(self,request):
        source = request.GET.get('src', '0')
        destination = request.GET.get('dst', '0')
        print(destination)

        if source == '0' or destination == '0':
            return HttpResponse('please find source and destination')
        # source = source.lower()
        # destination = destination.lower()

        obj=Flight.objects.filter(source__city_name__iexact=source,destination__city_name__iexact=destination)
        if obj.count:
            return HttpResponse('No cities exit in database')
        #print(obj)
        result=[]

        for i in obj:

                #print("ADSasddsa")
                result.append({
                'airline_id' :  i.airline_id,
                'airline_name' : i.airline_name,
                })


        return HttpResponse(json.dumps(result), content_type='application/json')

'''class UserValidation(View):
    def post(self,request):
        email_id=request.POST['email_id']
        data=User.objects.all()
        c=0
        for i in data:
            if email_id==i.email_id:
                c=1
        if(c==1):
           return HttpResponse("User allready exit please move forward to create booking" )

        #flight=request.POST['flight']
        #obj=User(email_id=email_id,name=name,age=age,passport_id=passport_id)

        else :

           return HttpResponse('your account has not been created,  move forward to create user account')'''


class CreateUserAccount(View):
    def post(self,request):
        email_id=request.POST['email_id']
        name=request.POST['name']
        age=request.POST['age']
        passport_id=request.POST['passport_id']
        data=User.objects.all()
        c=0
        for i in data:
            if email_id==i.email_id:
                c=1
        if(c!=1):
            data=User(email_id=email_id,name=name,age=age,passport_id=passport_id)
            data.save()
            return HttpResponse("account created move forward to create booking")
        else:
            return HttpResponse("user allready exist")


class CreateBooking(View):
    def post(self,request):
        email_id=request.POST['email_id']
        flight_id=request.POST['flight_id']
        seats=request.POST['seats']
        email=User.objects.all()
        c=0
        for i in email:
            if i.email_id==email_id:
                name1=i.name
                c=1

        if c==1:
           obj=Flight.objects.filter(flight_id=flight_id)

           for i in obj:
                data=TicketDetails(person_name=name1,email_id=email_id,source=i.source.city_name,destination=i.destination.city_name,airline_name=i.airline_name,
                airline_id = i.airline_id,departure_date=i.departure_date,seats=seats)
                data.save()
           return HttpResponse("Booking successfully created ")
        else:
            return HttpResponse('user_id does not exit please make user account after that you can create booking')



class GetBookingDetails(View):
    def get(self,request):
        email_id = request.GET.get('user_id', 'null')

        if email_id == 'null':
            return HttpResponse('please provide correct user_id')
        else:
            result=[]
            obj=TicketDetails.objects.filter(email_id__iexact=email_id)
            for i in obj:
                result.append({
                'person_name' :  i.person_name,
                'airline_name' :  i.airline_name,
                'airline_id' :  i.airline_id,
                'source' :  (i.source),
                'destination' :  (i.destination),
                'departure_date' : str(i.departure_date),
                'seats' :  i.seats,

                })


            return HttpResponse(json.dumps(result), content_type='application/json')

class GetAirlineDetails(View):
    def get(self,request):
        airline_name = request.GET.get('airline_name', 'null')

        if airline_name == 'null':
            return HttpResponse('please provide correct airline_name')
        else:
            result=[]
            data=Flight.objects.filter(airline_name__iexact=airline_name)
            for i in data:
                print (i.source)
                result.append({
                'flight_id' :  i.flight_id,
                'airline_name' :  i.airline_name,
                'airline_id' :  i.airline_id,
                'source' :  i.source.city_name,
                'destination' :  i.destination.city_name,
                'departure_date' : str(i.departure_date),
                'total_seats' :  i.total_seats,

                })
            return HttpResponse  (json.dumps(result), content_type='application/json')
