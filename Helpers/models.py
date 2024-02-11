from django.db import models
from Admin.models import *
from Guest.models  import *
# Create your models here.

class tbl_post(models.Model):
    post_image=models.FileField(upload_to="Post/")
    post_content=models.CharField(max_length=50)
    post_request=models.ForeignKey(tbl_request,on_delete=models.CASCADE) 
    helpers=models.ForeignKey(tbl_helper,on_delete=models.CASCADE)
    

class tbl_advertisement(models.Model):
    ad_title=models.CharField(max_length=50)
    ad_image=models.FileField(upload_to="Advertisements/")  
    ad_content=models.CharField(max_length=50)
    ad_contact=models.CharField(max_length=50)
    helpers=models.ForeignKey(tbl_helper,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default=0,null=True)
