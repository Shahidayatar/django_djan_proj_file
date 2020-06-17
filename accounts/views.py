from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth # we import this to create user model,, auth is used for login

# Create your views here.
def login(request):
    if request.method=='POST': # 'method ' cannot be in capital
        username = request.POST['username']
        password = request.POST['password']


        user=auth.authenticate(username=username,password=password) # this is in inbuilt in django google it.. we created a user object.
        if user is not None:
            auth.login(request,user)# we are giving access to user  #https://www.youtube.com/watch?v=teaeVbcT9BI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=109
            return redirect( "/") # slash goes back or back to html page
        else :
            messages.info(request,'invalid credential')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        Username = request.POST['Username']
        Email = request.POST['Email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
           if User.objects.filter(username=Username).exists():# we are cheching if username is same
                messages.info(request,'username taken') # this way we print the error on the same page... you can use error instead of info
                return redirect('register')
               #print("username taken ... try another")   #this way we print the message on console..cooment the abpve and see in the python console


           elif User.objects.filter(email=Email).exists():
               messages.info(request, 'email taken')
               return redirect('register')
               #print("email already exist , try another!! ")#this way we print the message on console..cooment the abpve and see in the python console

           else:
                user=User.objects.create_user(username=Username,first_name=first_name,password=password1,email=Email,last_name=last_name)
                user.save(); #  this way we save the user
                print("user created")
                return redirect('login')

        else:
            print("password not matching!!")
            return render('register')
        return redirect('/')  # we are going back from register to home page

    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')