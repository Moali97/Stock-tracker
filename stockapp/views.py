from django.shortcuts import render
from .forms import StockForm
import requests
from .models import StockList

headers = {
        'Content-Type': 'application/json',
        'Authorization' : '14dfe59b364eb4d7ad9a62a03bfda423b3031073'
}


def home(request):
   url = "https://api.tiingo.com/tiingo/daily/{}/prices"
   response = requests.get(url,headers=headers)



    name = StockList.objects.all()
    form = StockForm
    context = {'form': form, 'name': name}
    return render(request, 'home.html', context)
