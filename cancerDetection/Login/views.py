from django.http import HttpResponse
from django.shortcuts import render
from .models import LoginModel
def Login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        rs = LoginModel(emailid=email,password=password)
        rs.save()
        return HttpResponse("yeah Data inserted")
    return render(request,'login.html')