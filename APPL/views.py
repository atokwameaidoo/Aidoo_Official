from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index (request):
    return HttpResponse ("<h1>THIS IS THE OFFICIAL WEBSITE FOR EMMANUEL KWAME AIDOO. <BR> CHIEF TECHNOLOGY OFFICER AND LEAD ENGINEER OF ASTRA, <BR>THE WORLD'S BEST ELECTRIC CAR MANUFACTURING COMPANY. <BR> WEBSITE CURRENTLY UNDER MAINTENANCE.</h1>")
