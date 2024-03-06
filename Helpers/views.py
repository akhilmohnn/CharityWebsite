from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from Guest.models import *
from Organization.models import *

# Create your views here.

def homepage(request):
    hdata=tbl_helper.objects.get(id=request.session['hid'])
    return render(request,"Helpers/Homepage.html",{'hdata':hdata})

def myprofile(request):
    if 'hid' in request.session:
        hdata=tbl_helper.objects.get(id=request.session['hid'])
        return render(request,"Helpers/MyProfile.html",{'hdata':hdata})
    else :
        return redirect("Guest:login")

def changep(request):
    hdata=tbl_helper.objects.get(id=request.session['hid'])
    if request.method=="POST":
        pwd=hdata.helper_password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                hdata.helper_password=pass1
                hdata.save()
                return redirect("Helpers:ChangePassword")
            else:
                msg="password  does not match"
                return render(request,"Helpers/ChangePassword.html",{'msg':msg})
        else:
            msg="incorrect password"
            return render(request,"Helpers/ChangePassword.html",{'msg':msg})
    else:
        return render(request,"Helpers/ChangePassword.html")
    

def editprofile(request):
    hdata=tbl_helper.objects.get(id=request.session['hid'])
    if request.method=="POST":
        hdata.helper_name=request.POST.get("txt_name")
        hdata.helper_contact=request.POST.get("txt_con")
        hdata.helper_email=request.POST.get("txt_email")
        hdata.helper_address=request.POST.get("txt_address")
        hdata.save()
        return redirect("Helpers:MyProfile")
    else:
        return render(request,"Helpers/EditProfile.html",{'hdata':hdata})   
 
    
def postproduct(request):
    request_data=tbl_request.objects.all()
    post=tbl_post.objects.all()
    hdata=tbl_helper.objects.get(id=request.session['hid'])
    if request.method=="POST":
        image=request.FILES.get("post_image")
        content=request.POST.get("post_content")

        rqst=tbl_request.objects.get(id=request.POST.get('post_request'))

        tbl_post.objects.create(post_image=image,post_content=content,post_request=rqst,helpers=hdata)

        return render(request,'Helpers/Post.html',{'rqst':request_data,'post': post,'post': post})
    else:
        return render(request,'Helpers/Post.html',{'rqst':request_data,'post': post,'post': post})
    
def deleteproduct(request,did):
    tbl_post.objects.get(id=did).delete()
    return redirect("Helpers:PostProduct") 


def viewrequest(request):
    rqst1=tbl_helprequest.objects.filter(status=1)
    return render(request,"Helpers/ViewRequest.html",{'rqst1':rqst1}) 

def requestfull(request,aid):
    rdata=tbl_helprequest.objects.get(id=aid)
    return render(request,"Helpers/RequestFull.html",{'rdata':rdata}) 

# def rqstfull(request,aid):
#     rdata=tbl_helprequest.objects.get(id=aid)
#     return render(request,"Helpers/MyProfile.html",{'hdata':rdata})

def search(request):
    district_data=tbl_district.objects.all()
    type_data=tbl_type.objects.all()
    odata=tbl_organization.objects.filter(status=1)

    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        
        return render(request,'Helpers/Search.html',{'district':district_data,'type':type_data,'odata':odata})
    else:
           return render(request,'Helpers/Search.html',{'district':district_data,'type':type_data,'odata':odata})

def ajaxorg(request):
    if request.GET.get("tid")!="":
        typedata=tbl_type.objects.get(id=request.GET.get("tid"))
        if request.GET.get("pid")!="":
            placedata=tbl_place.objects.get(id=request.GET.get("pid"))
            data=tbl_organization.objects.filter(org_type=typedata,org_place=placedata,status=1)
            return render(request,"MedicalShop/Ajaxorg.html",{'data':data})
        elif request.GET.get("did")!="":
            districtdata=tbl_district.objects.get(id=request.GET.get("did"))
            data=tbl_organization.objects.filter(org_type=typedata,org_place__district_id=districtdata,status=1)
            return render(request,"MedicalShop/Ajaxorg.html",{'data':data})
        else:
            data=tbl_organization.objects.filter(org_type=typedata,status=1)
            return render(request,"MedicalShop/Ajaxorg.html",{'data':data})
    else:
        if request.GET.get("pid")!="":
            placedata=tbl_place.objects.get(id=request.GET.get("pid"))
            data=tbl_organization.objects.filter(org_place=placedata,status=1)
            return render(request,"MedicalShop/Ajaxorg.html",{'data':data})
        else:
            districtdata=tbl_district.objects.get(id=request.GET.get("did"))
            data=tbl_organization.objects.filter(org_place__district_id=districtdata,status=1)
            return render(request,"MedicalShop/Ajaxorg.html",{'data':data})
        

def booking(request):
    helpdata=tbl_helper.objects.get(id=request.session["hid"])
    odata=tbl_book.objects.filter(post_id__helpers=helpdata,status=0)
    
    return render(request,"Helpers/Bookings.html",{'odata':odata})        

def acceptedbooking(request):
    helpdata=tbl_helper.objects.get(id=request.session["hid"])
    odata=tbl_book.objects.filter(post_id__helpers=helpdata,status=1)
    
    return render(request,"Helpers/AcceptedBookings.html",{'odata':odata})   


def rejectedbooking(request):
    helpdata=tbl_helper.objects.get(id=request.session["hid"])
    odata=tbl_book.objects.filter(post_id__helpers=helpdata,status=2)
    
    return render(request,"Helpers/RejectedBookings.html",{'odata':odata})   

def acceptbooking(request,aid):
    data=tbl_book.objects.get(id=aid)
    data.status=1
    data.save()
    return redirect("Helpers:booking")

def rejectbooking(request,rid):
    data=tbl_book.objects.get(id=rid)
    data.status=2
    data.save()
    return redirect("Helpers:booking")

def advertisement(request):
    ad=tbl_advertisement.objects.all()
    hdata=tbl_helper.objects.get(id=request.session['hid'])  
    addata=tbl_advertisement.objects.filter(helpers=hdata)
    if request.method=="POST":
        title=request.POST.get("ad_title")
        image=request.FILES.get("ad_image")
        content=request.POST.get("ad_content")
        contact=request.POST.get("ad_contact")

        tbl_advertisement.objects.create(ad_title=title,ad_image=image,ad_content=content,ad_contact=contact,helpers=hdata)

        return render(request,'Helpers/Advertisement.html',{'ad':ad,'addata':addata}) 
    else:
        return render(request,'Helpers/Advertisement.html',{'ad':ad,'addata':addata})
    

def scholar(request):
    disdata=tbl_scholarshipname.objects.all()
    misdata=tbl_scholarshiptype.objects.all()
    if request.method=="POST":
        mat = tbl_scholarshiptype.objects.get(id=request.POST.get("select_sch"))
        tbl_scholarshipname.objects.create(scholarship_name=request.POST.get("txt_name1"),scholarship_details=request.POST.get("txt_name2"),
        
        scholarship_type=mat)
        return render(request,"Helpers/Scholarship.html",{'disdata':disdata,'misdata':misdata})
    else:

        return render(request,"Helpers/Scholarship.html",{'disdata':disdata,'misdata':misdata})
    
def viewscholarapply(request):
    orgdata=tbl_scholarshipapply.objects.all()
    return render(request,"Helpers/ViewScholarApply.html",{'orgdata':orgdata})

def acceptscholar(request,did):
    data=tbl_scholarshipapply.objects.get(id=did)
    data.status=1
    data.save()
    return redirect("Helpers:ViewScholarApply")


def rejectscholar(request,did):
    data=tbl_scholarshipapply.objects.get(id=did)
    data.status=2
    data.save()
    return redirect("Helpers:ViewScholarApply")    

def add_pay(request,did):
    data=tbl_advertisement.objects.get(id=did)
    if request.method=="POST":
        data.status=3
        data.save()
        return redirect("Helpers:advertisement")
    else:
        return render(request,"Helpers/Payment.html") 
def paynow(request,did):
    data=tbl_helprequest.objects.get(id=did)
    if request.method=="POST":
        data.status=3
        data.save()
        return redirect("Helpers:viewrequest")
    else:
        return render(request,"Helpers/Payment.html") 

def donatenow(request,did):
    data=tbl_helprequest.objects.get(id=did)
    data.status=2
    data.save()
        
    return redirect("Helpers:viewrequest")
    













   

