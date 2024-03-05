from django.urls import path
from Helpers import views

app_name='Helpers'
urlpatterns = [
     path('homepage/',views.homepage,name="Homepage"),
     path('myprofile/',views.myprofile,name="MyProfile"),
     path('changepwd/',views.changep,name="ChangePassword"),
     path('editprofile/',views.editprofile,name="EditProfile"),
     path('postproduct/',views.postproduct,name="PostProduct"),
     path('deleteproduct/<int:did>',views.deleteproduct,name="deleteproduct"),
     path('viewrequest/',views.viewrequest,name="viewrequest"),
     
     path('requestfull/<int:aid>',views.requestfull,name="requestfull"),
     path('search/',views.search,name="search"),
     path('ajaxorg/',views.ajaxorg,name="ajaxorg"),
     path('booking/',views.booking,name="booking"),
     path('acceptedbooking/',views.acceptedbooking,name="acceptedbooking"),
     path('rejectedbooking/',views.rejectedbooking,name="rejectedbooking"),

     path('acceptbooking/<int:aid>',views.acceptbooking,name="acceptbooking"),
     path('rejectbooking/<int:rid>',views.rejectbooking,name="rejectbooking"),
     path('advertisement/',views.advertisement,name="advertisement"),
     path('scholarship/',views.scholar,name="Scholarship"),
     path('ViewScholarApply/',views.viewscholarapply,name="ViewScholarApply"),
     path('acceptscholar/<int:did>',views.acceptscholar,name="acceptscholar"),
     path('rejectscholar/<int:did>',views.rejectscholar,name="rejectscholar"),
      path('addpay/<int:did>',views.add_pay,name="ad_pay"),
     
     
]
