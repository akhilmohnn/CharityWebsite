from django.db import models
from Guest.models import *
from Admin.models import *
from Helpers.models import *

# Create your models here.
 
class tbl_helprequest(models.Model):
    req_price=models.CharField(max_length=50)
    req_content=models.CharField(max_length=50)
    req_proof=models.FileField(upload_to="Requests/")
    req_request=models.ForeignKey(tbl_request,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default=0,null=True) 

class tbl_book(models.Model):
    book_name=models.CharField(max_length=50)
    book_address=models.CharField(max_length=50)
    book_contact=models.CharField(max_length=50)
    post_id=models.ForeignKey(tbl_post,on_delete=models.CASCADE) 
    organization_id=models.ForeignKey(tbl_organization,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)

class tbl_scholarshipapply(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to="Orgdoc/")
    scholarship_name=models.ForeignKey(tbl_scholarshipname,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    org_name=models.ForeignKey(tbl_organization,on_delete=models.SET_NULL,null=True)

class tbl_complaint(models.Model):  
    complainttitle=models.CharField(max_length=50)
    complainttype=models.ForeignKey(tbl_comptype,on_delete=models.CASCADE) 
    content=models.CharField(max_length=50)
    complaintdate=models.DateField(auto_now_add=True) 
    organization=models.ForeignKey(tbl_organization,on_delete=models.SET_NULL,null=True)
      
    
