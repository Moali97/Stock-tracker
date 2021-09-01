from django.shortcuts import render
from .forms import StockForm
import requests



def home(request):
    url = "https://api.tiingo.com/tiingo/daily/<ticker>/prices"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '14dfe59b364eb4d7ad9a62a03bfda423b3031073'
    }
    requestresponse = requests.get(url, headers=headers)

    form = StockForm
    context = {'form': form}
    return render(request, 'home.html', context)
