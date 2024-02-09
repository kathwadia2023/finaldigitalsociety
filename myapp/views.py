from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from digital_soceity import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
# import requests
import random



# Create your views here.
def index(request):
    msg = ''
    if request.method == 'POST':
        newuser = signup_form(request.POST)
        if newuser.is_valid():
            email_user=newuser.cleaned_data.get('email')
            try:
                signupmaster.objects.get(email=email_user)
                print("Email user is already exists!")
                msg="Email user is already exists!"
            except signupmaster.DoesNotExist:
                               
                print("Signup Successfully!")
                msg="Signup Successfully!"
               
                global fotp
                fotp = random.randint(10000,99999)
               
                # OTP mail
                subject = 'Your OTP Verfication'
                message = f"Hi your OTP is {fotp}, thank you for choosing us"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [ request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
               
                temp= {
                "name":request.POST["firstname"],
                "email":request.POST["email"],
                "password":request.POST["password"],
                }
                newuser.save()
                return render(request,'otp_verify.html')
            else:
                print(newuser.errors)

        elif request.POST.get('login')=='login':
            email_u = request.POST['email']
            pswd = request.POST['password']
            r =request.POST['role']

            user=signupmaster.objects.filter( email = email_u, password=pswd,role=r)           
            c_id = signupmaster.objects.get(email = email_u)
            print("Current ID:",c_id.id)
            c_role=c_id.role
            print("Current Role:",c_role)

            if user:
               
                print("login Success")
                # msg = "login Success"
                status = True
                request.session['user']= email_u
                request.session['uid'] = c_id.id
                request.session['c_role']= c_role
                return redirect("member_page")
            else:
                print("Login fail ,plz try again!!!")

    
        else:
            print(newuser.errors)
            msg="Something went wrong...Try again!"
    return render(request, 'index.html',{'msg':msg})


def otp(request):
    global fotp
    global msg
    if request.method=="POST":

        if request.POST['otp'] == str(fotp):
             return redirect("index")

        else:
            return render(request,'otp_verify.html',{'msg':'OTP not match'})
    else :
        return render(request,'index.html')


def go_green(request):
    return render(request, 'go_green.html')

def contact_us(request):
    if request.method == "POST":
        newfeedback = contact_form(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Feedback saved")
            
        # send mail
            sub="Inquiry Received"
            message = f"Hello {request.POST['name']}! \n\nWe have Received Your Inquiry.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nDigital Society PVT. LTD.\n Mo: +91 95866 32371"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
        else:
            print(newfeedback.errors)
    return render(request, 'contact.html')

def event(request):
    return render(request, 'event.html')

def com_member(request):
    return render(request, 'com_member.html')


def member_page(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data = global_notice.objects.all()
    # data=appointment.objects.all()
    return render(request, 'member_page.html', {'c_role':c_role, 'user':user, 'data':data, 'id':id})


def resetpass(request):
    msg = ""
    status = False
    if request.method == "POST":
        email_f = request.POST['email']
        mob_f = request.POST['mobile']
        try:
            user = signupmaster.objects.get(email=email_f, mobile=mob_f)
            uid = user.id
            print("User id:", uid)
            request.session['uid']=uid
            status=True
            print("Email and Mobile number found...")
            msg = 'Email and Mobile number found...'
            return redirect('newpass')
        except:
            print("Error! Not Found...")
            msg = "Sorry! not found plz try again"
    return render(request, 'resetpass.html', {'msg':msg, 'status':status})


def newpass(request):
    uid = request.session.get('uid')
    cuid = signupmaster.objects.get(id = uid)
    if request.method == 'POST':
        new_pass = update_form(request.POST)
        if new_pass.is_valid():
            new_pass = update_form(request.POST, instance=cuid)
            new_pass.save()
            print("Password is updated")
            return redirect('/')
        else:
            print("Error!!!!")
    return render(request, 'newpass.html')



def profile(request):
    user=request.session.get('user') 
    uid=request.session.get('uid')
    cuser=signupmaster.objects.get(id=uid)
    if request.method=='POST':
        newuser=update_profile(request.POST,instance=cuser)
        if newuser.is_valid():
            newuser.save()
            print("Profile updated!")
            return redirect("member_page")
        else:
            print(newuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})



def residence_detail(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data_det= signupmaster.objects.all()

    return render(request, 'residence_det.html', {'c_role':c_role, 'user':user, 'data':data_det})


def complaint_reg(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=complaint.objects.all()
    # p_id = complaint.objects.get(id = id)
    # p_data = complaint.objects.all()
    if request.method=='POST':
        comp=complaint_form(request.POST, request.FILES)
        if comp.is_valid():
            comp.save()
            print("Your Complaint has been submitted!")
            # send mail
            sub="Complaint Submitted!"
            message = f"Hello ! \n\nYour Complaint is Submited!!! .\n\nIf any Queries, plz feel free to contact us...\nRegards \nDigital Soceity PVT. LTD.\n Mo: +91 95866 32371"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect("member_page")
        else:
            print(comp.errors)
            print("Sorry Try again")
    return render(request, 'complaint.html', {'c_role':c_role, 'user':user, 'data':data})

def status_up(request,id):
    stid = complaint.objects.get(id=id)
    if request.method=='POST':
        data=complaint_update(request.POST,instance=stid)
        if data.is_valid(): #true
            data.save()
            print("Your data has been updated!")
            return redirect('complaint')
        else:
            print(data.errors)
    return render(request,'status_update.html',{'stid':stid})



def maintenance_pay(request): 
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=maintenance.objects.all()
   
    if request.method == "POST":
        pat_app = maint_form(request.POST, request.FILES)
        if pat_app.is_valid():
            pat_app.save()
            print("Payment Maintenance saved")
            # send mail
            sub="Payment!!! Thank you"
            message = f"Hello {request.POST['name']}! \n\nYour Payment is Done!!! .\n\nIf any Queries, plz feel free to contact us...\nRegards \nDigital Soceity PVT. LTD.\n Mo: +91 95866 32371"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect("member_page")
        else:
            print(pat_app.errors)
            print("Sorry Try again")
    return render(request, 'maintenance.html', {'c_role':c_role, 'user':user, 'data':data, 'id':id})


def inq_data(request):
     
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=contact.objects.all()
    return render(request, 'inquiry_data.html', {'c_role':c_role, 'user':user, 'data':data })


def global_mail(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=global_notice.objects.all()
    data_signup = signupmaster.objects.all()
    mail_data = []
    for i in data_signup:
        mail_data.append(i.email)
    print(mail_data)    
    if request.method == "POST":
        notice = global_notice_form(request.POST)
        if notice.is_valid():
            notice.save()
            print("notice is save")
            # send mail
            sub="Notice !!!"
            message = request.POST['notice']
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=mail_data
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect("member_page")
        else:
            print(notice.errors)
    return render(request, 'global_mail_send.html', {'c_role':c_role, 'user':user, 'data':data, 'data_signup':data_signup })    

def user_logout(request):
    logout(request)
    return redirect('/')


