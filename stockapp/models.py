from django.db import models


class StockList(models.Model):
    name = models.CharField(max_length=250, default='')