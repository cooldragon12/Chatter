from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,"Chat_App/index.html")

