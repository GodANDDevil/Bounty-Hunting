from django.shortcuts import render
from .models import Scout, Seeker
# Create your views here.

def index(request):
    return render(request, 'Index.html')

def LoginScout(request):
    return render(request, 'LoginScout.html')

def LoginSeeker(request):
    return render(request, 'LoginSeeker.html')

def RegisterScout(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        number = request.POST.get('number')
        text = request.POST.get('text')
        reg_no = request.POST.get('reg_no')
        data=Scout(scout_Company_name=company_name,
                   scout_gmail=gmail,
                   scout_password=password,
                   scout_phone=number,
                   scout_address=text,
                   scout_reg_no=reg_no
                   )
        data.save()
        return render(request, 'LoginScout.html')
    return render(request, 'RegisterScout.html')

def RegisterSeeker(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        number = request.POST.get('phone_numbr')
        text = request.POST.get('text')
        citi_no = request.POST.get('cetr_no')
        dof = request.POST.get('dof')
        data=Seeker(seeker_Full_name=full_name,
                    seeker_gmail=gmail,
                    seeker_password=password,
                    seeker_phone=number,
                    seeker_address=text,
                    seeker_citi_no=citi_no,
                    seeker_dof=dof
                    )
        data.save()
        return render(request, 'LoginSeeker.html')
    return render(request, 'RegisterSeeker.html')

def login_index(request):
    return render(request, 'Index.html')
