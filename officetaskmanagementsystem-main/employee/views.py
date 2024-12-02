from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')    

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.post['firstname']
        ln = request.post['lastname']
        ec = request.post['empcode']
        em = request.post['email']
        pwd = request.post['password']

        try:
            User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(empcode = ec)
            error="no"
        except:
            error="yes"
    return render(request, 'registration.html') 