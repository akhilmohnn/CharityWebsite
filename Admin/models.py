from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district_id=models.ForeignKey(tbl_district,on_delete=models.CASCADE) 

class tbl_type(models.Model):
    type_name=models.CharField(max_length=50)  

class tbl_request(models.Model):
    request_name=models.CharField(max_length=50)

# class tbl_orgverification(models.Model):
#     name=models.CharField(max_length=50)  
#     email=models.CharField(max_length=50)
#     contact=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)
#     logo=models.FileField(upload_to="Orgdoc/")
#     proof=models.FileField(upload_to="Orgdoc/")
#     type=models.CharField(max_length=50)
#     status=models.CharField(max_length=50,default=0,null=True)






         
    
         