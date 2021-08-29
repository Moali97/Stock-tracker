from django.shortcuts import render
from .forms import StockForm


def home(request):
    form = StockForm
    context = {'form': form}
    return render(request, 'home.html', context)
