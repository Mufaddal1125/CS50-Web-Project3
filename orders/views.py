from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.core.exceptions import *
from .forms import RegisterForm, LoginForm
from .models import *


# Create your views here.
def index(request):

    if request.session.get('userName') is not None:
        sessionuser = {'firstname': request.session.get('firstname'), 'lastname': request.session.get('lastname'),
                'user': request.session.get('userName')}
        return render(request, "index.html", {'user': sessionuser})
    return render(request, "index.html")


def register(request):
    form = RegisterForm()
    message(request, form)
    # if request Method post Submit the form
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        # check if user already exists
        user = Users.objects.filter(userName=request.POST['user_name']).first()
        if user is not None:
            request.session['message'] = "User already Exists"
            return HttpResponseRedirect('/login')

        # check if email already exists
        email = Users.objects.filter(emailAddress=request.POST['email']).first()
        if email:
            request.session['message'] = "Email Already Exists"
            return HttpResponseRedirect('/login')

        # validate the form
        if form.is_valid():
            user = Users(userName=form.cleaned_data['user_name'], password=form.cleaned_data['password'],
                         emailAddress=form.cleaned_data['email'],
                         firstName=form.cleaned_data['first_name'],
                         lastName=form.cleaned_data['last_name'])
            user.save()

            request.session['message'] = "Created Account Successfully"
            return HttpResponseRedirect('/login')

    # redirect to form
    return render(request, 'register.html', {'form': form})


def login(request):
    form = LoginForm()

    # check if form is submitted
    if request.method == 'POST':
        # check if user exist
        user = Users.objects.filter(userName=request.POST['user_name'], password=request.POST['password']).first()
        if user:
            request.session['userName'] = user.userName
            request.session['firstname'] = user.firstName
            request.session['lastname'] = user.lastName

            return HttpResponseRedirect('/')
        else:
            request.session['message'] = "Error Invalid Credentials"
            return HttpResponseRedirect('/login')

    # check if user already logged in
    if request.session.get('user'):
        return HttpResponseRedirect('/')

    # render login page with Message
    message(request, form)
    return render(request, 'login.html', {'form': form})


def message(request, form):
    if request.session.get('message'):
        message = str(request.session.get('message'))
        del request.session['message']
        return render(request, 'login.html', {'message': message, 'form': form})


def logout(request):
    if request.session.get('userName'):
        del request.session['userName']
        del request.session['firstname']
        del request.session['lastname']
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect('/login')
