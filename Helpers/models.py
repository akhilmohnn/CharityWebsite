from django.db import models
from Admin.models import *
from Guest.models  import *
# Create your models here.

class tbl_post(models.Model):
    post_image=models.FileField(upload_to="Post/")
    post_content=models.CharField(max_length=50)
    post_request=models.ForeignKey(tbl_request,on_delete=models.CASCADE) 
    helpers=models.ForeignKey(tbl_helper,on_delete=models.CASCADE)
    
 
