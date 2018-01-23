from django.shortcuts import render, redirect
from models import *

def index(request):
		
	return render(request, 'courses/index.html', {'courses': Course.objects.all()})

def create(request):
	Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
	return redirect('/')

def remove(request, id):
	print '&'*15
	return render(request, 'courses/destroy.html', {'courses': Course.objects.get(id=id)})


def destroy(request, id):

	destroy = Course.objects.get(id=id)
	destroy.delete()

	return redirect('/')