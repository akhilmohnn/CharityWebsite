from django.urls import path
from MedicalShop import views

app_name='MedicalShop'
urlpatterns = [
     
     path('homepage/',views.homepage,name="homepage"),
     path('viewrequest/',views.viewrequest,name="viewrequest"),
     
     path('requestfull/<int:aid>',views.requestfull,name="requestfull"),
     
     path('postproduct/',views.postproduct,name="PostProduct"),

     path('search/',views.search,name="search"),

      path('ajaxorg/',views.ajaxorg,name="ajaxorg"),
     



     


     


]