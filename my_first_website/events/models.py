from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Address', max_length=300)
    zip_code = models.CharField('Zip/Post Code', max_length=10)
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField("First Name", max_length=40)
    last_name = models.CharField("Last Name", max_length=40)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField('Manager', max_length=60)
    attendees = models.ManyToManyField(User, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
