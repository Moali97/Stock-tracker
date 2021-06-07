from django.shortcuts import render
import requests


def home(request):
    url = "https://api.covid19api.com/summary"

#    payload = {}
#    headers = {}

    response = requests.request.get( url).json()
#                                     , headers=headers, data=payload)

    print(response.text)

    return render(request, 'home.html')
