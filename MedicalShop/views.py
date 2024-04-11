from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from Guest.models import *
from Helpers.models import *
from Organization.models import *

def viewrequest(request):
    rqst1=tbl_helprequest.objects.filter(status=1)
    return render(request,"MedicalShop/ViewRequest.html",{'rqst1':rqst1}) 

def requestfull(request,aid):
   
    rdata=tbl_helprequest.objects.get(id=aid)
    return render(request,"MedicalShop/RequestFull.html",{'rdata':rdata}) 

# def viewrequest(request):
#     rqst1=tbl_helprequest.objects.filter(status=1)
#     return render(request,"Helpers/ViewRequest.html",{'rqst1':rqst1}) 

# def requestfull(request, aid):
#     rdata = tbl_helprequest.objects.get(id=aid)
#     return render(request, "Helpers/RequestFull.html", {'rdata': rdata})

def postproduct(request):
    request_data=tbl_request.objects.all()
    post=tbl_post.objects.all()
    if request.method=="POST":
        image=request.FILES.get("post_image")
        content=request.POST.get("post_content")

        rqst=tbl_request.objects.get(id=request.POST.get('post_request'))

        tbl_post.objects.create(post_image=image,post_content=content,post_request=rqst)

        return render(request,'MedicalShop/Post.html',{'rqst':request_data,'post': post,'post': post})
    else:
        return render(request,'MedicalShop/Post.html',{'rqst':request_data,'post': post,'post': post})
    

def search(request):
    district_data=tbl_district.objects.all()
    type_data=tbl_type.objects.all()
    odata=tbl_organization.objects.filter(status=1)

    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        
        return render(request,'MedicalShop/Search.html',{'district':district_data,'type':type_data,'odata':odata})
    else:
           return render(request,'MedicalShop/Search.html',{'district':district_data,'type':type_data,'odata':odata})

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


def homepage(request):
    mdata=tbl_medicalshop.objects.get(id=request.session['mid'])
    return render(request,"MedicalShop/Homepage.html",{'mdata':mdata})     

def myprofile(request):
    if 'mid' in request.session:
        mdata=tbl_medicalshop.objects.get(id=request.session['mid'])
        return render(request,"MedicalShop/MyProfile.html",{'mdata':mdata})
    else :
        return redirect("Guest:login")

def editprofile(request):
    mdata=tbl_medicalshop.objects.get(id=request.session['mid'])
    if request.method=="POST":
        mdata.medical_name=request.POST.get("txt_name")
        mdata.medical_contact=request.POST.get("txt_con")
        mdata.medical_email=request.POST.get("txt_email")
        mdata.medical_address=request.POST.get("txt_address")
        mdata.save()
        return redirect("MedicalShop:MyProfile")
    else:
        return render(request,"MedicalShop/EditProfile.html",{'mdata':mdata}) 
    
def changep(request):
    mdata = tbl_medicalshop.objects.get(id=request.session['mid'])
    
    if request.method == "POST":
        pwd = mdata.medical_password
        current_pwd = request.POST.get("txt_pass")
        
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            
            if pass1 == pass2:
                mdata.medical_password = pass1
                mdata.save()
                return redirect("MedicalShop:ChangePassword")
            else:
                msg = "password does not match"
                return render(request, "MedicalShop/ChangePassword.html", {'msg': msg})
        else:
            msg = "incorrect password"
            return render(request, "MedicalShop/ChangePassword.html", {'msg': msg})
    
    # Add a default return statement here
    return render(request, "MedicalShop/ChangePassword.html") 

def paynow(request,did):
    data=tbl_helprequest.objects.get(id=did)
    if request.method=="POST":
        data.status=3
        data.save()
        return redirect("MedicalShop:runpayment")
    else:
        return render(request,"MedicalShop/Payment.html") 

def donatenow(request,did):
    data=tbl_helprequest.objects.get(id=did)
    data.status=2
    data.save()
        
    return redirect("MedicalShop:viewrequest")
    
def runpayment(request):
    return render(request,"MedicalShop/runpayment.html")

def paysucessful(request):
    return render(request,"MedicalShop/paysucessfull.html")



