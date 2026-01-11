from django.shortcuts import render,redirect
from .models import Scout, Seeker, JobPost, Index_Scout_Images, Index_Seeker_Images, Ads_Images, Login_Images, Register_Images

# Create your views here.

def index(request):
    seeker_img = Index_Seeker_Images.objects.filter(index_seeker_img__isnull=False)
    scout_img = Index_Scout_Images.objects.filter(index_scout_img__isnull=False)

    return render(request, 'Index.html', {'seeker_img':seeker_img, 'scout_img':scout_img})

def LoginScout(request):
    login_img = Login_Images.objects.filter(login_img__isnull=False)
    if request.method == "POST":
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        
            # Add authentication logic here
        try:
            user = Scout.objects.get(scout_gmail=gmail)
            if user.scout_password == password:
                request.session['scout__Company_name']=user.scout_Company_name
                return redirect('HomepageScout')
            else:
                return render(request, 'LoginScout.html', {'error_message': 'Invalid password'})
        except Scout.DoesNotExist:
            return render(request, 'LoginScout.html', {'error_message': 'User does not exist'})
            
    return render(request, 'LoginScout.html',{'login_img':login_img})

def LoginSeeker(request):
    login_img = Login_Images.objects.filter(login_img__isnull=False)
    if request.method == "POST":
        name = request.POST.get('full_name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        try:
            user = Seeker.objects.get(seeker_gmail=gmail)
            if user.seeker_password == password:
                request.session['seeker_Full_name']=user.seeker_Full_name
                return redirect('HomepageSeeker')
            else:
                return render(request, 'LoginSeeker.html', {'error_message': 'Invalid password'})
        except Seeker.DoesNotExist:
            return render(request, 'LoginSeeker.html', {'error_message': 'User does not exist'})
        
    return render(request, 'LoginSeeker.html',{'login_img':login_img})

def RegisterScout(request):
    register_img = Register_Images.objects.filter(register_img__isnull=False)
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        number = request.POST.get('number')
        text = request.POST.get('address')
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
    return render(request, 'RegisterScout.html',{'register_img':register_img})

def RegisterSeeker(request):
    register_img = Register_Images.objects.all()
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        number = request.POST.get('phone_numbr')
        text = request.POST.get('address')
        citi_no = request.POST.get('cert_no')
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
    return render(request, 'RegisterSeeker.html', {'register_img': register_img})

def HomepaheSeeker(request):
    jobs = JobPost.objects.all()
    seeker_Full_name = request.session.get('seeker_Full_name')
    search_job = request.GET.get('search_job')
    if not seeker_Full_name:
        return redirect('LoginSeeker')
    seeker = Seeker.objects.get(seeker_Full_name=seeker_Full_name)
    if search_job:
        data = JobPost.objects.filter(job_title=search_job)
        return render(request, 'HomepageSeeker.html', {'jobs': data})
    return render(request, 'HomepageSeeker.html', {'seeker': seeker, 'jobs': jobs})

def HomepageScout(request):
    jobs = JobPost.objects.all()
    scout_Company_name = request.session.get('scout__Company_name')

    if not scout_Company_name:
        return redirect('LoginScout')
    scout = Scout.objects.get(scout_Company_name=scout_Company_name)
    return render(request, 'HomepageScout.html',{'scout': scout, 'jobs': jobs})

def AboutUs(request):
    return render(request, 'AboutUs.html')

def ContactUs(request):
    return render(request, 'ContactUs.html')

def PostJob(request):
    if request.method == "POST":
        scout_Company_name = request.session.get('scout__Company_name')
        company_name = Scout.objects.get(scout_Company_name=scout_Company_name)
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        job = JobPost(
            job_poasted_by=company_name,
            job_title=title,
            job_description=description,
            job_location=location,
            job_salary=salary
        )
        job.save()
        return redirect('HomepageScout')
    return render(request, 'PostJob.html')

def Apply(request):
    return render(request, 'Apply.html')

def login_index(request):
    return render(request, 'Index.html')
