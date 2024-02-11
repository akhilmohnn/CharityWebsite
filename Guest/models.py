from django.db import models
from Admin.models import *

# Create your models here.

class tbl_helper(models.Model):
    helper_name=models.CharField(max_length=50)
    helper_email=models.CharField(max_length=50)
    helper_contact=models.CharField(max_length=50)
    helper_address=models.CharField(max_length=50)
    helper_photo=models.FileField(upload_to="Helpdoc/")
    helper_type=models.ForeignKey(tbl_type,on_delete=models.CASCADE)
    helper_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    helper_password=models.CharField(max_length=50)

class tbl_organization(models.Model):
    org_name=models.CharField(max_length=50)
    org_email=models.CharField(max_length=50)
    org_contact=models.CharField(max_length=50)              
    org_address=models.CharField(max_length=50)
    org_logo=models.FileField(upload_to="Orgdoc/")
    org_proof=models.FileField(upload_to="Orgdoc/")
    org_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    org_type=models.ForeignKey(tbl_type,on_delete=models.CASCADE)
    org_password=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default=0,null=True)

class tbl_medicalshop(models.Model):
    medical_name=models.CharField(max_length=50)
    medical_email=models.CharField(max_length=50)
    medical_contact=models.CharField(max_length=50)
    medical_address=models.CharField(max_length=50)
    medical_photo=models.FileField(upload_to="MedicalDoc/")
    medical_proof=models.FileField(upload_to="MedicalDoc/")
    medical_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    medical_password=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default=0,null=True)
    

              
