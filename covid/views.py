from django.shortcuts import render
import requests


def home(request):
    url = "https://api.covid19api.com/summary"

    country = 'Albania'

    response = requests.get(url.format(country)).json()

#    print(response)

    stats = {
        'country': country,
        'total': response['Global']['NewConfirmed'],
        'new': response['Global'][0]['NewDeaths'],
    }

    context = {'stats': stats}

    return render(request, 'home.html', context)
