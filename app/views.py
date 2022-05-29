from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = UserRegistration(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	form = UserRegistration()
	context = {
		'form': form
	}
	return render(request,'app/index.html',context)
	