from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pyexpat.errors import messages

from .models import User
from .models import Theatre
from .form import CustomerRegistration
from .models import User1
from .models import User2
from .form import Signup
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import LoginForm




def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def second(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())

def third(request):
    movie = Theatre.objects.all().values()
    template = loader.get_template('theatre.html')
    context = {
        'movie': movie,
    }
    return HttpResponse(template.render(context,request))


def fourth(request):
    if request.method == 'POST':
        fm = CustomerRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mn = fm.cleaned_data['movie']
            th = fm.cleaned_data['theatre']
            tt = fm.cleaned_data['time']
            dt = fm.cleaned_data['date']
            reg = User(name=nm, email=em, movie=mn, theatre=th, time=tt, date=dt)
            reg.save()
            print(nm)
            print(em)
            print(mn)
            print(th)
            print(tt)
            print(dt)
    else:
        fm = CustomerRegistration()
    return render(request, 'registration.html', {'form':fm})



from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def fifth(request):
    if request.method == 'POST':

        # read whatever your HTML already has
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = request.POST.get('contact')

        subject = "Complain"
        to = "kalpandeishwari@gmail.com"

        msg = f"Hello {name},\nComplain: {message}\nContact: {contact}\nEmail: {email}"

        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to], fail_silently=False)

        return render(request, 'contact.html')

    return render(request, 'contact.html')


from django.contrib.auth.models import User
from .form import Signup

def seventh(request):
    if request.method == 'POST':
        fm = Signup(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            un = fm.cleaned_data['user_name']
            pw = fm.cleaned_data['password']

            user = User.objects.create_user(
                username=un,
                email=em,
                password=pw
            )
            user.first_name = nm
            user.save()

            return redirect('login')

    else:
        fm = Signup()

    return render(request, 'signup.html', {'form': fm})




def eighth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')        # Home page URL name
    else:
        form = LoginForm()

    return render(request, 'loginform.html', {'form': form})





