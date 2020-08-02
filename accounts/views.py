from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username', False)
        email = request.POST['email']
        passw = request.POST['passw']
        conf_pass = request.POST['conf_pass']

        if passw == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username = username, password = passw, email = email, first_name = first_name, last_name = last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'passwords naut matching')
            return redirect('register')

    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, "invalid credentials owo")
            return redirect("login")

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def choose(request):
    return render(request, "choose.html")

def admin(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username', False)
        email = request.POST['email']
        passw = request.POST['passw']
        conf_pass = request.POST['conf_pass']

        if passw == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('admin')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('admin')

            else:
                user = User.objects.create_user(username = username, password = passw, email = email, first_name = first_name, last_name = last_name)
                user = is_superuser
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'passwords naut matching')
            return redirect('admin')

    else:
        return render(request, "admin.html")

def newad(request):
    return render(request, 'newad.html')

def feegen(request):
    if request.method=='POST':
            adfee = int(request.POST.get('adfee', False))
            exfee = int(request.POST.get('exfee', False))
            ict = int(request.POST.get('ict', False))
            medfee = int(request.POST.get('medfee', False))
            recfee = int(request.POST.get('recfee', False))
            tutfee = int(request.POST.get('tutfee', False))
            tranfee = int(request.POST.get('tranfee', False))

            x = adfee+exfee+ict+medfee+recfee+tutfee+tranfee
            return render(request, "feeresult.html", {"fee":x})
    else:
        return render(request, 'feegen.html')
    


def feeresult(request):
    return render

def parsec(request):
    pass

def teacher(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username', False)
        email = request.POST['email']
        passw = request.POST['passw']
        conf_pass = request.POST['conf_pass']

        if passw == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('teacher')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('teacher')

            else:
                user = User.objects.create_user(username = username, password = passw, email = email, first_name = first_name, last_name = last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'passwords naut matching')
            return redirect('teacher')

    else:
        return render(request, "teacher.html")
