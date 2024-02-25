from django.urls import path
from Admin import views
app_name="webbasic"


urlpatterns = [
       path('district/',views.district,name="district"),
       path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),
       path('deletedistrict/<int:delid>',views.deletedistrict,name="deletedistrict"),
       path('place/',views.place,name="place"),
       path('editplace/<int:eid>',views.editplace,name="editplace"),
       path('deleteplace/<int:delid>',views.deleteplace,name="deleteplace"),
       path('type/',views.type,name="type"),
       path('edittype/<int:eid>',views.edittype,name="edittype"),
       path('deletetype/<int:did>',views.deletetype,name="deletetype"),
       path('requesttype/',views.reqtype,name="requesttype"),
       path('deletereqtype/<int:did>',views.deletereqtype,name="deletereqtype"),
       path('orgverification/',views.orgverification,name="orgverification"),
       path('acceptedorg/',views.acceptedorg,name="AcceptedOrganisation"),
       path('rejectedorg/',views.rejectedorg,name="RejectedOrganisation"),

        path('acceptorgn/<int:aid>',views.acceptorg,name="acceptorg"),
        path('rejectorgn/<int:rid>',views.rejectorg,name="rejectorg"),

        path('viewrequest/',views.viewrequest,name="viewrequest"),

        path('acceptedrequest/',views.acceptedrequest,name="AcceptedRequest"),
        path('rejectedrequest/',views.rejectedrequest,name="RejectedRequest"),
        path('acceptrequest/<int:aid>',views.acceptrequest,name="acceptrequest"),
        path('rejectrequest/<int:rid>',views.rejectrequest,name="rejectreq"),
        path('viewadverisement/',views.viewadverisement,name="viewadverisement"),
        path('acceptedads/',views.acceptedads,name="acceptedads"),
        path('rejectedads/',views.rejectedads,name="rejectedads"),
        path('acceptads/<int:aid>',views.acceptads,name="acceptads"),
        path('rejectads/<int:rid>',views.rejectads,name="rejectads"),
        path('Scholarshiptype/',views.scholarshiptype,name="scholarshiptype"),
        path('ComplaintType/',views.comptype,name="ComplaintType")






]