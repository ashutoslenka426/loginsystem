from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

def index(request):
	return render(request , 'loginapp/index.html')

# process form data
def signup(self , request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username , password=password)

			if user is not None:

				if user.is_active:
					login(request , user)
					return redirect('')

		return render(request, self.template_name, {'form': form})

