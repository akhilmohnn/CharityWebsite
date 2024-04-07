from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

# Create your views here.

    
def newhelper(request):
        district_data= tbl_district.objects.all()
        place_data=tbl_place.objects.all()
        type_data=tbl_type.objects.all()
        if request.method=="POST":
             name=request.POST.get("helper_name")
             email=request.POST.get("helper_email")
             contact=request.POST.get("helper_contact")
             address=request.POST.get("helper_address")
             photo=request.FILES.get("helper_photo")
             password=request.POST.get("helper_password")

             place=tbl_place.objects.get(id=request.POST.get('sel_place'))
             type=tbl_type.objects.get(id=request.POST.get('helper_type'))

             tbl_helper.objects.create(helper_name=name,helper_place=place,helper_type=type,helper_email=email,helper_contact=contact,helper_address=address,helper_photo=photo,helper_password=password)

             return render(request,'Guest/Helper.html',{'district':district_data,'place':place_data,'type':type_data})
        else:
             return render(request,'Guest/Helper.html',{'district':district_data,'place':place_data,'type':type_data})
        
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district_id=dis)
    return render(request,"Guest/AjaxPlace.html",{"place":place})  

def neworganization(request):
      district_data=tbl_district.objects.all()    
      place_data=tbl_place.objects.all()
      type_data=tbl_type.objects.all()
      if request.method=="POST":
            name=request.POST.get("org_name")
            email=request.POST.get("org_email")
            contact=request.POST.get("org_contact")
            address=request.POST.get("org_address")
            logo=request.FILES.get("org_logo")
            proof=request.FILES.get("org_proof")
            password=request.POST.get("org_password")  

            place=tbl_place.objects.get(id=request.POST.get('sel_place'))
            type=tbl_type.objects.get(id=request.POST.get('org_type'))

            tbl_organization.objects.create(org_name=name,org_email=email,org_contact=contact,org_address=address,org_logo=logo,org_proof=proof,org_password=password,org_place=place,org_type=type)

            return render(request,'Guest/Organization.html',{'district':district_data,'place':place_data,'type':type_data})
      else:
           return render(request,'Guest/Organization.html',{'district':district_data,'place':place_data,'type':type_data})
      
def newmedicalshop(request):
      district_data=tbl_district.objects.all()
      place_data=tbl_place.objects.all()
      if request.method=="POST":
            name=request.POST.get("medical_name")
            email=request.POST.get("medical_email")
            contact=request.POST.get("medical_contact")
            address=request.POST.get("medical_address")
            photo=request.FILES.get("medical_photo")
            proof=request.FILES.get("medical_proof")
            password=request.POST.get("medical_password")

            place=tbl_place.objects.get(id=request.POST.get('sel_place'))

            tbl_medicalshop.objects.create(medical_name=name,medical_email=email,medical_contact=contact,medical_address=address,medical_photo=photo,medical_proof=proof,medical_password=password,medical_place=place) 
            return render(request,'Guest/MedicalShop.html',{'district':district_data,'place':place_data})  
      else:
            return render(request,'Guest/MedicalShop.html',{'district':district_data,'place':place_data})  


      

def login(request):
      if request.method=="POST":
            email=request.POST.get("log_email")
            password=request.POST.get("log_password")

            helpercount=tbl_helper.objects.filter(helper_email=email,helper_password=password).count()

            orgcount=tbl_organization.objects.filter(org_email=email,org_password=password,status=1).count()

            medcount=tbl_medicalshop.objects.filter(medical_email=email,medical_password=password).count()

            if helpercount > 0:
                  helperdata=tbl_helper.objects.get(helper_email=email,helper_password=password)
                  request.session['hid']=helperdata.id
                  return redirect('Helpers:Homepage')
            
            elif orgcount > 0:
                  orgdata=tbl_organization.objects.get(org_email=email,org_password=password)
                  request.session['oid']=orgdata.id
                  return redirect('Organization:Homepage')
            
            elif medcount> 0:
                  meddata=tbl_medicalshop.objects.get(medical_email=email,medical_password=password)
                  request.session['mid']=meddata.id
                  return redirect('MedicalShop:homepage')
            
            else:
                  msg="Invalid credentials!!"
                  return render(request,'Guest/Login.html',{'msg':msg})
      else:
            return render(request,'Guest/Login.html')


def index(request):
      return render(request,"Guest/index.html")