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
    # change 'symbol' to 'q' like in yahoo docs, then put 'q={}' in url above
    querystring = {'symbol': 'TSLA'}
    # querying database
    allstocks = StockList.objects.all()

    stock_data =[]

    querystring = {'symbol': 'AAPL'}
    response = requests.get(url, headers=headers, params=querystring).json()

        # dictionary of information to be displayed on templates
        stock = {
            'name': querystring,
            'price': response['price']['regularMarketOpen'],
        }
        stock_data.append(stock)

    print(stock_data)

    form = StockForm

    # context has form and dictionary
    context = {'form': form, 'stock_data': stock_data}
    return render(request, 'home.html', context)
