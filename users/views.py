from django.shortcuts import render

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def login(request):
    msg = ""
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # 1. check username is present in db
        if User.objects.filter(username = username).exists():
            
            # 2. if user exists -- authenticate - (checks password and username)
            user = authenticate(request, username=username, password=password)
            # 3. if password/username is correct
            if user:
                # login(user)
                msg = "Login Success"
            else:
                msg = "Invalid Username/Password" 
        else:
            msg = "User not found with this username or userid"
    return render(request, "users/login.html", {"msg":msg})


def register(request):
    msg=""

    if request.method == "POST" :
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        all_existingregister= User.objects.filter(username=username)
    

        if len(all_existingregister) > 0 :
            msg="username already exists",username

        if not username :
            msg="username must not be empty"

        if not password :
            msg="password must not be empty"

        if not firstname :
            msg="firstname must not be empty"

        if not lastname :
            msg="lastname must not be empty"

        if not email :
            msg="email must not be empty"

    

        
        
       
        else :

            User.objects.create(
            firstname = firstname,
            lastname = lastname,
            username = username,
            password = password,
            email = email,
            
        )
            print("register succesfully" )

    return render(request, "register.html", {"msg": msg})

