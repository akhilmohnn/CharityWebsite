from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from Guest.models import *
from Helpers.models import *

# Create your views here.

def homepage(request):
    odata=tbl_organization.objects.get(id=request.session['oid'])
    return render(request,"Organization/Homepage.html",{'odata':odata})

def myprofile(request):
    odata=tbl_organization.objects.get(id=request.session['oid'])
    return render(request,"Organization/MyProfile.html",{'odata':odata})

def editprofile(request):
    odata=tbl_organization.objects.get(id=request.session['oid'])
    if request.method=="POST":
        odata.org_name=request.POST.get("txt_name")
        odata.org_contact=request.POST.get("txt_con")
        odata.org_email=request.POST.get("txt_email")
        odata.org_address=request.POST.get("txt_address")
        odata.save()
        return redirect("Organization:MyProfile")
    else:
        return render(request,"Organization/EditProfile.html",{'odata':odata})  

def changep(request):
    odata=tbl_organization.objects.get(id=request.session['oid'])
    if request.method=="POST":
        pwd=odata.org_password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                odata.org_password=pass1
                odata.save()
                return redirect("Organization:ChangePassword")
            else:
                msg="password  does not match"
                return render(request,"Organization/ChangePassword.html",{'msg':msg})
        else:
            msg="incorrect password"
            return render(request,"Organization/ChangePassword.html",{'msg':msg})
    else:
        return render(request,"Organization/ChangePassword.html")    


def reqproduct(request):
    request_data=tbl_request.objects.all()
    rqst1=tbl_helprequest.objects.all()
    if request.method=="POST":
        price=request.POST.get("req_price")
        content=request.POST.get("req_content")
        proof=request.FILES.get("req_proof") 

        rqst=tbl_request.objects.get(id=request.POST.get('req_request'))

        tbl_helprequest.objects.create(req_proof=proof,req_content=content,req_price=price,req_request=rqst)

        return render(request,'Organization/Requests.html',{'rqst':request_data,'rqst1': rqst1,'rqst1': rqst1})
    else:
        return render(request,'Organization/Requests.html',{'rqst':request_data,'rqst1': rqst1,'rqst1': rqst1})
    

def viewposts(request):
    rqst1=tbl_post.objects.all()
    return render(request,"Organization/ViewPost.html",{'rqst1':rqst1})

def bookfull(request, bid):
    post = tbl_post.objects.get(id=bid)
    odata = tbl_organization.objects.get(id=request.session['oid'])
    if request.method == "POST":
        name = request.POST.get("book_name")
        address = request.POST.get("book_address")
        contact = request.POST.get("book_contact")

        tbl_book.objects.create(book_name=name, book_address=address, book_contact=contact, organization_id=odata,post_id=post)
        
        return render(request, "Organization/BookFull.html", {'post': post, 'odata': odata}) 
    else:
        return render(request, "Organization/BookFull.html", {'post': post, 'odata': odata})
    
def mybook(request):
    odata=tbl_book.objects.all()
    return render(request,"Organization/MyBooking.html",{'odata':odata})

def vscholarship(request):
    disdata=tbl_scholarshiptype.objects.all()
    subcat=tbl_scholarshipname.objects.all()
    if request.method=="POST":
        return render(request,"Organization/ViewScholarship.html",{'disdata':disdata,'subcat':subcat})
    else:
        return render(request,"Organization/ViewScholarship.html",{'disdata':disdata,'subcat':subcat})
    
def ajaxscholar(request):
    scholardata=tbl_scholarshiptype.objects.get(id=request.GET.get('sch'))
    scholarnamedata=tbl_scholarshipname.objects.filter(scholarship_type=scholardata)
    return render(request,"Organization/ajaxscholar.html",{'subcat':scholarnamedata})    

def schapply(request,schid):

    schdata=tbl_scholarshipname.objects.get(id=schid)
    if 'oid' in request.session:
        data=tbl_organization.objects.get(id=request.session["oid"])
        if request.method=="POST" and request.FILES:
            tbl_scholarshipapply.objects.create(org_name=data,scholarship_name=schdata,
         
            document=request.FILES.get('filedoc'))
            return render(request,"Organization/ScholarshipApply.html",{'data':data,'schdata':schdata})
        else:
           # return render(request,"Member/scholarshipapply.html")
            return render(request,"Organization/ScholarshipApply.html",{'data':data,'schdata':schdata})


    
    
  
