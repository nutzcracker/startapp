from django.http import HttpResponse
from .models import Bb
from django.template import loader
from django.shortcuts import render
# Create your views here.

def index(request):
	bbs = Bb.objects.all()
	return render(request, 'bboard/index.html', {'bbs' : bbs })