from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from Guest.models import *
from Helpers.models import *
from Organization.models import *

def viewrequest(request):
    type=tbl_request.objects.get(id=5)
    rqst1=tbl_helprequest.objects.filter(status=1,req_request=type,)
    return render(request,"MedicalShop/ViewRequest.html",{'rqst1':rqst1}) 

def requestfull(request,aid):
   
    rdata=tbl_helprequest.objects.get(id=aid)
    return render(request,"MedicalShop/RequestFull.html",{'rdata':rdata}) 

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