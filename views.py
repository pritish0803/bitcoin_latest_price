# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

def index(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, "bitcoin/index.html", data)
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=100"
    try:
        data=requests.get(api_url).json
    except Exception as e:
        print(e)
        data=dict()
    return data

# Create your views here.
