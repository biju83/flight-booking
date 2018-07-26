# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from application.models import Flight,City,User,TicketDetails
admin.site.register(Flight)
admin.site.register(City)
admin.site.register(User)
admin.site.register(TicketDetails)
# Register your models here.
