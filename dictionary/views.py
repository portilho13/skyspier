import csv
import datetime
import json

# Import API
from opensky_api import OpenSkyApi


from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from .models import Aircraft
# Create your views here.

# Def api

api = OpenSkyApi()

def index(request):
    return render(request, "dictionary/index.html")

"""
Function to save Aircrafts to Database:


def insert(request):
    with open("aircraftDatabase.csv") as file:
        lines = csv.DictReader(file)
        count = 0
        for line in lines:
            aircraft = Aircraft(
                icao24 = line["icao24"],
                registration = line["registration"],
                manufacturericao = line["manufacturericao"],
                manufacturername = line["manufacturername"],
                model = line["model"],
                typecode = line["typecode"],
                serialnumber = line["serialnumber"],
                linenumber = line["linenumber"],
                icaoaircrafttype = line["icaoaircrafttype"],
                operator = line["operator"],
                operatorcallsign = line["operatorcallsign"],
                operatoricao = line["operatoricao"],
                operatoriata = line["operatoriata"],
                owner = line["owner"],
                testreg = line["testreg"],
                registered = line["registered"],
                reguntil = line["reguntil"],
                status = line["status"],
                built = line["built"],
                firstflightdate = line["firstflightdate"],
                seatconfiguration = line["seatconfiguration"],
                engines = line["engines"],
                modes = line["modes"],
                adsb = line["adsb"],
                acars = line["acars"],
                notes = line["notes"],
                categoryDescription = line["categoryDescription"]
            )
            aircraft.save()
            count += 1
        print(f"Sucess, saved {count} to database.")
    return render(request, "dictionary/insert.html")
"""

def aircraft(request, id):
    aircraft = get_object_or_404(Aircraft, id=id)

    ### Get age
    if aircraft.built:
        reg_date = datetime.datetime.now() - datetime.datetime.strptime(aircraft.built, '%Y-%m-%d')
        age = reg_date.days // 365
    else:
        age = None

    # Past 21 days

    past = datetime.datetime.now() - datetime.timedelta(days=21)

    # Request for api

    flights = api.get_flights_by_aircraft(str(aircraft.icao24), int(past.timestamp()), int(datetime.datetime.now().timestamp()))

    # Transform to JSON
    id = 0
    flight_data = []
    flightsJson = []
    if flights:
        for flight in flights:
            first_seen = flight.firstSeen
            last_seen = flight.lastSeen
        
            if first_seen is not None:
                first_seen_utc = datetime.datetime.utcfromtimestamp(first_seen)
            else:
                first_seen_utc = None
            
            if last_seen is not None:
                last_seen_utc = datetime.datetime.utcfromtimestamp(last_seen)
            else:
                last_seen_utc = None
            
            duration = None
            if first_seen_utc and last_seen_utc:
                duration = last_seen_utc - first_seen_utc
                durationMinutes = duration.total_seconds() / 60

            # Get dates First Seen
            
            DateFirstSeen, HourFirstSeen = str(first_seen_utc).split(" ")
            hourFirst, minuteFirst, secoundFirst = HourFirstSeen.split(":")

            # Get Dates Last Seen

            DateLastSeen, HourLastSeen = str(last_seen_utc).split(" ")
            hourLast, minuteLast, secoundLast = HourLastSeen.split(":")

            # Flight Date

            flight_date = first_seen_utc.strftime('%d %B %Y')
            id += 1

            flight_info = {
                "id": id,
                "firstSeenHour": hourFirst,
                "firstSeenMinute": minuteFirst,
                "lastSeenHour": hourLast,
                "lastSeenMinute": minuteLast,
                "duration": int(durationMinutes),
                "date": flight_date
            }
            flight_data.append(flight_info)


    
    return render(request, "dictionary/aircraft.html", {
        "aircraft": aircraft,
        "age": age,
        "flights": zip(flights or [], flight_data)
    })
    
def database(request, value):
    aircrafts = Aircraft.objects.filter(Q(registration__icontains=value) | Q(operator__icontains=value)).distinct()
    return JsonResponse([aircraft_info.serialize() for aircraft_info in aircrafts], safe=False)

@csrf_exempt
def redirect_flight(request):
    if request.method == "POST":
        icao24 = request.POST["icao24"]
        firstSeen = int(request.POST["firstSeen"])
        lastSeen = int(request.POST["lastSeen"])
    
    track = api.get_track_by_aircraft(icao24, lastSeen)
    latitude = []
    longitude = []
    altitude = []

    for s in track.path[::-1]:
        i = int(s[3] * 3.28)
        altitude.append({"label": ".", "y": i})
    
    return render(request, "dictionary/flight.html", {
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude
    })

def grafico(request):
    user_data_2020 = [
        { "label": "JAN", "y": 58200 },
        { "label": "FEB", "y": 59110 },
        { "label": "MAR", "y": 60320 },
        { "label": "APR", "y": 61440 },
        { "label": "MAY", "y": 62580 },
        { "label": "JUN", "y": 63190 },
        { "label": "JUL", "y": 64000 },
        { "label": "AUG", "y": 64290 },
        { "label": "SEP", "y": 65530 },
        { "label": "OCT", "y": 65300 },
        { "label": "NOV", "y": 65340 },
        { "label": "DEC", "y": 64530 }
    ]
    user_data_2021 = [
        { "label": "JAN", "y": 65100 },
        { "label": "FEB", "y": 66210 },
        { "label": "MAR", "y": 66540 },
        { "label": "APR", "y": 66680 },
        { "label": "MAY", "y": 67500 },
        { "label": "JUN", "y": 68850 },
        { "label": "JUL", "y": 69000 },
        { "label": "AUG", "y": 70130 },
        { "label": "SEP", "y": 71050 },
        { "label": "OCT", "y": 71500 },
        { "label": "NOV", "y": 72110 },
        { "label": "DEC", "y": 71820 }
    ]
    return render(request, "dictionary/grafico.html", { "user_data_2021": user_data_2021, "user_data_2020": user_data_2020 })
