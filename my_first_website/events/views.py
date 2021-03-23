from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

# Create your views here.


def index(request):
    return HttpResponse(f"<h1> Welcome to a brand new Django App </h1> <p style='padding:12px'> In this application, we will demonstrate how the Django RestAPI Framework works. </p>")
