from django.shortcuts import render
from .forms import StockForm
import requests
from .models import StockList

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "3be7f48f16msh9bcc8b5167481bdp110da2jsn49023f5afc93"
}


def home(request):
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile'

    querystring = {'symbol': 'AAPL'}
    response = requests.get(url, headers=headers, params=querystring).json()

     print(response.text)


     form = StockForm
     context = {'form': form}
     return render(request, 'home.html', context)
