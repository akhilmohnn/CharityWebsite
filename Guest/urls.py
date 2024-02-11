from django.urls import path,include
from Guest import views

app_name="Guest"
urlpatterns = [
        path('helperregistration/',views.newhelper,name="newhelper"),
        path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
        path('orgregistration/',views.neworganization,name="neworganization"),
        path('login/',views.login,name="login"),
        path('medicalregistration/',views.newmedicalshop,name="newmedicalshop"),
        path('',views.index,name="index"),
]