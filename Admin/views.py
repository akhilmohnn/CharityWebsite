from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Organization.models import *
# Create your views here.

def district(request):
    district_data=tbl_district.objects.all()
    if request.method=="POST":
        datacount=tbl_district.objects.filter(district_name=request.POST.get("district")).count()
        if datacount>0:
            return render(request,"Admin/District.html",{'dis':district_data})
        else:
            tbl_district.objects.create(district_name=request.POST.get("district"))
        return render(request,"Admin/District.html",{'dis':district_data})
    else:
        return render(request,"Admin/District.html",{'dis':district_data})
       

def deletedistrict(request,delid):
    tbl_district.objects.get(id=delid).delete()
    return redirect("webbasic:district") 

def editdistrict(request,eid):
    district=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        district.district_name=request.POST.get("district")
        district.save()
        return redirect("webbasic:district")
    else:
        return render(request,"Admin/District.html",{'dis_data':district})
    

def place(request):
    dis = tbl_district.objects.all()
    plc = tbl_place.objects.all()
    if request.method=="POST":
        plc1 = tbl_district.objects.get(id=request.POST.get('dropdown')) 
        tbl_place.objects.create(district_id=plc1,place_name=request.POST.get("place"))
        return render(request,"Admin/place.html",{"district":dis,"plc1":plc})
    else:
        return render(request,"Admin/Place.html",{"district":dis,"plc1":plc})      
    
def editplace(request,eid):
    place=tbl_place.objects.get(id=eid)
    district=tbl_district.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('dropdown'))
        place.place_name=request.POST.get('place')
        place.district=district
        place.save()
        return redirect("webbasic:place")
    else:
        return render(request,"Admin/Place.html",{'editplace':place,'district':district})
    
def deleteplace(request,delid):
    tbl_place.objects.get(id=delid).delete()
    return redirect("webbasic:place") 

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district_id=dis)
    return render(request,"Guest/AjaxPlace.html",{"place":place}) 

def type(request):
    type_data=tbl_type.objects.all()
    if request.method=="POST":
        tbl_type.objects.create(type_name=request.POST.get("type"))
        return render(request,"Admin/Type.html",{'typ':type_data})
    else:
        return render(request,"Admin/Type.html",{'typ':type_data})
    
def edittype(request,eid):
    type=tbl_type.objects.get(id=eid)
    if request.method=="POST":
        type.type_name=request.POST.get("type")
        type.save()
        return redirect("webbasic:type")
    else:
        return render(request,"Admin/type.html",{'type_data':type})


def deletetype(request,did):
    tbl_type.objects.get(id=did).delete()
    return redirect("webbasic:type")

def reqtype(request):
    reqtype_data=tbl_request.objects.all()
    if request.method=="POST":
        tbl_request.objects.create(request_name=request.POST.get("reqtype"))
        return render(request,"Admin/Request.html",{'reqtype': reqtype_data})
    else:
        return render(request,"Admin/Request.html",{'reqtype': reqtype_data})
    
def deletereqtype(request,did):
    tbl_request.objects.get(id=did).delete()
    return redirect("webbasic:requesttype")

def orgverification(request):
    odata=tbl_organization.objects.filter(status=0)
    return render(request,"Admin/OrgVerification.html",{'odata':odata})

def acceptedorg(request):
    odata=tbl_organization.objects.filter(status=1)
    return render(request,"Admin/AcceptedOrganisation.html",{'odata':odata})



def rejectedorg(request):
    odata=tbl_organization.objects.filter(status=2)
    return render(request,"Admin/RejectedOrganisation.html",{'odata':odata})

def acceptorg(request,aid):
    orgdata=tbl_organization.objects.get(id=aid)
    orgdata.status=1
    orgdata.save()
    return redirect("webbasic:orgverification")

def rejectorg(request,rid):
    orgdata=tbl_organization.objects.get(id=rid)
    orgdata.status=2
    orgdata.save()
    return redirect("webbasic:orgverification")

def viewrequest(request):
    rqst1=tbl_helprequest.objects.filter(status=0)
    return render(request,"Admin/ViewRequests.html",{'rqst1':rqst1})

def acceptedrequest(request):
    rqst1=tbl_helprequest.objects.filter(status=1)
    return render(request,"Admin/AcceptedRequest.html",{'rqst1':rqst1})

def rejectedrequest(request):
    rqst1=tbl_helprequest.objects.filter(status=2)
    return render(request,"Admin/RejectedRequest.html",{'rqst1':rqst1})

def acceptrequest(request,aid):
    rqst=tbl_helprequest.objects.get(id=aid)
    rqst.status=1
    rqst.save()
    return redirect("webbasic:viewrequest")

def rejectrequest(request,rid):
    rqst=tbl_helprequest.objects.get(id=rid)
    rqst.status=2
    rqst.save()
    return redirect("webbasic:viewrequest")

def viewadverisement(request):
    addata=tbl_advertisement.objects.filter(status=0)
    return render(request,"Admin/ViewAdvertisement.html",{'addata':addata})

def acceptedads(request):
    addata=tbl_advertisement.objects.filter(status=1)
    return render(request,"Admin/Acceptedads.html",{'addata':addata})

def rejectedads(request):
    addata=tbl_advertisement.objects.filter(status=2)
    return render(request,"Admin/Rejectedads.html",{'addata':addata})

def acceptads(request,aid):
    addata1=tbl_advertisement.objects.get(id=aid)
    addata1.status=1
    addata1.save()
    return redirect("webbasic:viewadverisement")

def rejectads(request,rid):
    addata1=tbl_advertisement.objects.get(id=rid)
    addata1.status=2
    addata1.save()
    return redirect("webbasic:viewadverisement")

def scholarshiptype(request):
    disdata=tbl_scholarshiptype.objects.all()
    if request.method=="POST":
        tbl_scholarshiptype.objects.create(scholarship_type=request.POST.get("txt_scholar"))
        return render(request,"Admin/Scholarshiptype.html",{'scholarshiptype':disdata})
    else:
        return render(request,"Admin/Scholarshiptype.html",{'scholarshiptype':disdata})
    
def comptype(request):
    comptype_data=tbl_comptype.objects.all()
    if request.method=="POST":
        tbl_comptype.objects.create(complaint_name=request.POST.get("comptype"))
        return render(request,"Admin/ComplaintType.html",{'comptype': comptype_data})
    else:
        return render(request,"Admin/ComplaintType.html",{'comptype': comptype_data})  

def complaint(request):
    orgdata=tbl_organization.objects.get(id=request.session['oid'])
    comdata=tbl_comptype.objects.all()
    compdata=tbl_complaint.objects.all()
    return render(request,"Admin/ViewComplaint.html",{'orgdata':orgdata,'comdata':comdata,'compdata':compdata})

def homepage(request):
    return render(request,"Admin/Homepage.html")
   




    









    
    