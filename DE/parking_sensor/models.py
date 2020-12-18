from django.db import models

class Ahmedabad(models.Model):
    name = "Ahmedabad"
    place = models.CharField(max_length=50)
    total_spaces = models.CharField(max_length=5)
    vacancy = models.CharField(max_length=5)
class Gandhinagar(models.Model):
    name = "Gandhinagar"
    place = models.CharField(max_length=50)
    total_spaces = models.CharField(max_length=5)
    vacancy = models.CharField(max_length=5)

class Contact(models.Model):
    Name = models.CharField(max_length=25, default='Name')
    Email = models.EmailField()
    Subject = models.CharField(max_length=75, default='Subject')
    Contents = models.TextField(default='Please enter your message here',max_length=200)

class Booking(models.Model):
    Name = models.CharField(max_length=25)
    Mobile_no = models.IntegerField()
    response = models.CharField(max_length=25, default='null')