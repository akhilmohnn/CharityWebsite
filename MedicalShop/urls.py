from django.urls import path
from MedicalShop import views

app_name='MedicalShop'
urlpatterns = [
     
     path('homepage/',views.homepage,name="Homepage"),
     path('viewrequest/',views.viewrequest,name="viewrequest"),
     
     path('requestfull/<int:aid>',views.requestfull,name="requestfull"),
     
     path('postproduct/',views.postproduct,name="PostProduct"),

     path('search/',views.search,name="search"),

      path('ajaxorg/',views.ajaxorg,name="ajaxorg"),

      path('myprofile/',views.myprofile,name="MyProfile"),
      path('editprofile/',views.editprofile,name="EditProfile"),

      path('changepwd/',views.changep,name="ChangePassword"),
      path('paynow/<int:did>',views.paynow,name="paynow"),
     path('donatenow/<int:did>',views.donatenow,name="donatenow"),
  
     path('runpayment/',views.runpayment,name="runpayment"),
     path('paysucessful/', views.paysucessful,name="paysucessful"),
 
     



     


     


]