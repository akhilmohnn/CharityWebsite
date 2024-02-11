from django.urls import path
from Organization import views

app_name='Organization'
urlpatterns = [
     path('homepage/',views.homepage,name="Homepage"),
     path('myprofile/',views.myprofile,name="MyProfile"),
     path('changepwd/',views.changep,name="ChangePassword"),
     path('editprofile/',views.editprofile,name="EditProfile"),
     path('reqproduct/',views.reqproduct,name="reqproduct"),
     path('viewposts/',views.viewposts,name="viewposts"),
     path('bookfull/<int:bid>',views.bookfull,name="bookfull"),
     path('mybook/',views.mybook,name="mybook"),


     

    
]