from django.contrib import admin
from .models import Ahmedabad, Contact, Gandhinagar, Booking

class admindataA(admin.ModelAdmin):
    list_display = ['name', 'place', 'total_spaces','vacancy']

admin.site.register(Ahmedabad,admindataA)

class admindataG(admin.ModelAdmin):
    list_display = ['name', 'place', 'total_spaces','vacancy']

admin.site.register(Gandhinagar,admindataG)

class admincontact(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Subject', 'Contents']

admin.site.register(Contact,admincontact)

class adminbooking(admin.ModelAdmin):
    list_display = ['Name', 'Mobile_no', 'response']

admin.site.register(Booking,adminbooking)