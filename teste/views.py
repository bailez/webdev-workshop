from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def index(request):
    pessoas = Pessoa.objects.all()
    return render(request,'abcd.html', {'pess' : pessoas})
