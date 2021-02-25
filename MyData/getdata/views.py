from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse
import json
from getdata.models import Country

# Create your views here.

rapidapiKey = '724911062emshcc04191f9454015p1ff70cjsne1c328cbcabf'


def GetDailyReportsTotals(request):
    url = "https://covid-19-data.p.rapidapi.com/report/totals"
    querystring = {"date": "2020-07-21"}

    headers = {
        'x-rapidapi-key': rapidapiKey,
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)

    return HttpResponse(response)


def GetLatestCountryDataBycode(request):
    url = "https://covid-19-data.p.rapidapi.com/country/code"
    querystring = {"code": "it"}

    headers = {
        'x-rapidapi-key': rapidapiKey,
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)

    return HttpResponse(response)


def GetDailyReportByCountryCode(request):
    url = "https://covid-19-data.p.rapidapi.com/report/country/code"
    querystring = {"date": "2020-04-01", "code": "it"}

    headers = {
        'x-rapidapi-key': rapidapiKey,
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)

    return HttpResponse(response)


def ListCountires(request):
    url = "https://covid-19-data.p.rapidapi.com/help/countries"

    headers = {
        'x-rapidapi-key': rapidapiKey,
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.json())
    for data in response.json():
        c = Country.objects.get(name=data["name"],
                                alpha2code=data["alpha2code"],
                                alpha3code=data["alpha3code"],
                                latitude=data["latitude"],
                                longitude=data["longitude"])
        print(c)
        if not c:
            c = Country.objects.create(name=data["name"],
                                       alpha2code=data["alpha2code"],
                                       alpha3code=data["alpha3code"],
                                       latitude=data["latitude"],
                                       longitude=data["longitude"])
    return HttpResponse(response)


@login_required
def Dashboard(request):
    return render(request, 'getdata/home.html')
