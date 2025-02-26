from django.contrib import admin
from django.urls import path

from Administrator import views

app_name="Administrator"

urlpatterns = [

    path('AdminRegistration/',views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdmin/<int:delID>',views.delAdmin,name="delAdmin"),
    path('editAdminReg/<int:editID>',views.editAdminReg,name="editAdminReg"),

    path('ComplaintType/',views.ComplaintTypeInsertSelect,name="ComplaintTypeInsertSelect"),
    path('delcomplainttype/<int:delID>',views.delcomplainttype,name="delcomplainttype"),
    path('editcomplainttype/<int:editID>',views.editcomplainttype,name="editcomplainttype"),

    path('District/',views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:delID>',views.delDistrict,name="delDistrict"),
    path('editDistrict/<int:editID>',views.editDistrict,name="editDistrict"),

    path('Bloodgroup/',views.bloodgroupInsertSelect,name="bloodgroupInsertSelect"),
    path('delBlood/<int:delID>',views.delBlood,name="delBlood"),
    path('editBlood/<int:editID>',views.editBlood,name="editBlood"),

    path('Place/',views.placeInsertSelect,name="placeInsertSelect"),
    path('delplace/<int:delID>',views.delplace,name="delplace"),
    path('editplace/<int:editID>',views.editplace,name="editplace"),



]
