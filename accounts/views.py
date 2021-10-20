from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    #return HttpResponse('Success')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       # print(first_name,last_name,username,email)
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print('Username already Taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                print('This email already taken')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                print('User Created Successfully')
                return redirect('/')
        else:
            print('Password does not match')
            return redirect('register')
    else:
        return render(request,'register.html')
