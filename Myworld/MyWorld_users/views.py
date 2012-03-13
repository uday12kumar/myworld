from Myworld.MyWorld_users.models import UserProfiles
from django.contrib.auth import authenticate
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
import string , random
from django.core.mail import EmailMessage

def user_authentication(request):
    username_ =  request.POST["username"]
    password_ = request.POST["password"]
    user = authenticate(username= username_, password= password_)
    if user is not None:
        return HttpResponse(json.dumps("authinticated"),mimetype="application/json")
    else:
        return HttpResponse(json.dumps("incorrect username and password"),mimetype="application/json")
        
def add_user(request):
    email_ = request.POST["username"]
    udid_ = request.POST["udid"]
    name_ = request.POST["name"]
    generated_password = generate_password()
    user_django = User(username=email_,email=email_,first_name = name_)
    user_django.set_password(generated_password)
    user_django.save()
    user_object = UserProfiles(udid=udid_,user=user_django)
    user_object.save()
    send_mail(generated_password,email_)

def generate_password():
    genrator_string = string.digits+string.letters
    generated_password = "".join([random.choice(genrator_string) for el in range(10)])
    return generated_password

def send_mail(password,mail):
    body_ =  '''you have successfully added \n login with the following \n Username : 
    %s \n password : %s''' %(mail , password)
    email = EmailMessage(subject='Myworld Registration Successful', body=body_, to=['jayachand.potluri@mutualmobile.com','jayachand.potluri@gmail.com'])
    email.send()
    
    