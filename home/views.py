from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Film, Time, Seat
# Create your views here.


def index(request):
    data = Film.objects.all()
    seat = Seat.objects.all()
    print(seat)
    return render(request, "index.html", {"pro": data,"hide":seat})


def login(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        check = auth.authenticate(username=username, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect("/")
        else:
            msg = "Invalid Username Or Password"
            return render(request, "login.html", {"msg": msg})
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        ucheck = User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)
        if ucheck:
            msg = "Username Exits"
            return render(request, "register.html", {"msg": msg})
        elif echeck:
            msg = "Email Exits"
            return render(request, "register.html", {"msg": msg})
        elif password == "" or password != repassword:
            msg = "Invalid Password"
            return render(request, "register.html", {"msg": msg})
        else:
            user = User.objects.create_user(
                first_name=name, username=username, email=email, password=password)
            user.save()
            return redirect("/")
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def details(request):
    id = request.GET["id"]
    print(id)
    if request.method == "POST":
        data = Film.objects.filter(id=id)
        print(data)
        time = Time.objects.filter(pro_id=id)
        return render(request, "product.html", {"pro": data, "mtime": time,"new":id})


def selection(request):

    if request.method == "POST":
        broid=request.POST["broid"]
        data=Film.objects.filter(id=broid)
        time = request.POST["time"]
        seat = Seat.objects.filter(id=time)
    return render(request, "availability.html", {"mseat": seat,"pro":data})
    

def final(request):
    id=request.GET["id"]
    if request.method == "POST":
        broid=request.POST["broid"]
        print(broid)
        data=Film.objects.filter(id=broid)
        bata=Film.objects.get(id=broid)
        ticket=request.POST["ticket"]
        t=int(bata.price)-(int(bata.price)*int(bata.discount)/100)
        total=t*int(ticket)
        seat = Seat.objects.get(id=id)
        t1=int(seat.available)-int(ticket)
        Seat.objects.filter(id=id).update(available=t1)
        return render(request,"confirm.html",{"pro":data,"ticket":ticket,"total":total})


