from django.shortcuts import render

# Create your views here.

def about_fan(resquest):
    return render(resquest, 'about_fan.html')