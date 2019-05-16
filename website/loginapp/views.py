from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .forms import UserLoginForm


def index(request):
    return render(request, 'loginapp/index.html')


def success(request):
    return render(request, 'loginapp/index.html')


def successlogin(request):
    return render(request, 'loginapp/welcome.html')


class UserFormView(View):
    print("test entry")
    form_class = UserForm
    template_name = 'loginapp/index.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        print("test entry 1")
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class UserLoginFormView(View):

    print("test entry X")
    form_class = UserLoginForm
    template_name = 'loginapp/index.html'

    # process form data
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/successlogin/')

        return render(request, self.template_name, {'form': form})
