'''render html web pages'''
from django.http import HttpResponse
import random
from django.shortcuts import render
import joblib 

def home_view(request):
    return render(request, "home.html")

def result(request):
    cls = joblib.load('lm.pkl')
    lst = []
    lst.append(request.GET['Calcium'])
    lst.append(request.GET['Iron'])
    lst.append(request.GET['Sodium'])
    lst.append(request.GET['Vitamin A'])
    lst.append(request.GET['Vitamin C'])
    lst.append(request.GET['Cholestrol'])
    lst.append(request.GET['Protein'])
    lst.append(request.GET['Carbs'])
    lst.append(request.GET['Fats'])
    lst.append(request.GET['Sugars'])

    ans = cls.predict([lst])

    return render(request, "result.html", {"ans": ans})