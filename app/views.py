from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import USER
from django.conf import settings
from django.core.mail import send_mail



def index(request) : 
    return render(request,'index.html')

def login(request) :
    if request.method == 'POST' :
        try :
            temp = USER.objects.get(email = request.POST['email'])
            if request.POST['pass'] == temp.password :
                return render(request, 'index.html')
            return render(request, 'login.html', {'msg':'Incorrect Password !'})
        except : 
            return render(request, 'login.html', {'msg':'Email does not exist !'})
    return render(request,'login.html')

def about(request) :
    return render(request,'about.html')
def blogdetails(request) :
    return render(request,'blog-details.html')
def bloghome(request) : 
    return render(request,'blog-home.html')
def contact(request) :
    return render(request,'contact.html')
def departments(request) : 
    return render(request, 'departments.html')


def signup(request) :
    if request.method == 'POST' :
        try : 
            USER.objects.get(email= request.POST['email'])
            msg = 'Email already exists !'
            return render(request, 'signup.html',{'msg':msg} )

        except:
            if request.POST['pass'] == request.POST['cpass']:

                otp = random.randrange(1000,9999)
                subject = 'Welcome to the App'
                message = f'Your One Time Password (OTP) is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list ), 

                global info

                info = {
                    'fname' : request.POST['fname'],    
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'pass' : request.POST['pass']
                }
                
                return render(request, 'otp.html', {'msg':'OTP has been sent.','otp':otp})
            return render(request, 'signup.html',{'msg':'Both Passwords do not Match !'})        
    return render (request, 'signup.html')

def otp(request) :
    if request.method == 'POST' : 
        if request.POST['otp'] == request.POST['votp'] : 
            global info 
            USER.objects.create(
                fname= info['fname'],
                lname= info['lname'],
                mobile= info['mobile'],
                email= info['email'],
                password= info['pass']

            )
        
            return render(request, 'login.html', {'msg':'Account created Successfully .'})
        return render(request, 'otp.html', {'msg':'Invalid OTP','otp':request.POST['otp']})
    return render(request, 'signup.html')

def forgot_pass (request) : 
    if request.method == 'POST' : 
        try : 
            USER.objects.get(email = request.POST['email']),

            otp = random.randrange(1000,9999)
            subject = 'Welcome to the App'
            message = f'Your One Time Password (OTP) is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list ) 

            return render(request, 'forgot-otp.html',{'otp':otp})

        except : 
            return render(request,'forgot-pass.html', {'msg':'Email doest not Exist !'})
    return render(request,'forgot-pass.html')

def forgot_otp(request) :
    if request.method == 'POST' :
        if request.POST['otp'] == request.POST['votp'] : 

            return render(request, 'change-password.html')
    return render(request, 'forgot-otp.html')

def change_password(request) :
    if request.method == 'POST' :
            if request.POST['newpass']  == request.POST['cpass'] : 
                return render(request, 'login.html', {'msg':'Password Changed Successfully'})
            return redirect('change-password.html', {'msg':'Both Passwords do not Match !'})
    return redirect('change-password.html')