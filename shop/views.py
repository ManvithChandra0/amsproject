from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm, contactForm
from .models import Registration


# Create your views here.
def indexfunction(request):
    return render(request,"admindashbord.html")

def registration(request):
    form=RegistrationForm()

    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registration Failed")

    return render(request,"registration.html",{"form":form})

def userlogin(request):
    return render(request,"userlogin.html")

def checkuserlogin(request):
    emaild=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Registration.objects.filter( Q(email=emaild) & Q(password=pwd) )
    print(flag)

    if flag:
        user=Registration.objects.get(email=emaild)
        print(user)
        print(user.id,user.fullname,user.username) #other fields also
        request.session["uname"]=user.username
        return render(request,"home.html",{"uname":user.username})
    else:
        msg="Login Failed"
        return render(request,"userlogin.html",{"msg":msg})

def userhome(request):
    username=request.session["uname"]
    print(username)
    return render(request,"userhome.html",{"uname":username})

def contactform(request):
    form = contactForm()
    if request.method == "POST":
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Your Query Added successfully "
            return render(request,"contact.html",{"msg":msg,"deptform":form})
        else:
            msg = "Failed to Add query"
            return render(request, "contact.html", {"msg": msg,"deptform":form})
    return render(request,"contact.html",{"deptform":form})



def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def buyproducts(request):
    return render(request, 'vieweproducts.html')

def admindashbord(request):
    return render(request, 'admindashbord.html')

def service(request):
    return render(request, 'service.html')

