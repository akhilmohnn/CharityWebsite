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
     path('viewscholarship/',views.vscholarship,name="viewscholarship"),
     path('ajaxscholar/',views.ajaxscholar,name="ajaxscholar"),
     path('ScholarshipApply/<int:schid>',views.schapply,name="ScholarshipApply"),
     path('ViewScholarShipApply/',views.viewscholarshipapply,name="ViewScholarShipApply"),
     path('scholarshipstatus/', views.scholarshipstatus,name="scholarshipstatus"),
     path('complaints/',views.complaint,name="complaint"),
     path('helperstar/<int:hid>',views.starrating,name="helperrating"),
     path('ajaxstar/',views.ajaxstar,name="ajaxstar"),



     

    
]