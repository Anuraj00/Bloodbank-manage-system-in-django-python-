from django.shortcuts import render,redirect
from Administrator.models import *
# Create your views here.
#This Section AdminRegistration Opertions
def adminInsertSelect(request):
    admindata=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('txtphone')
        password=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=password)
        return render(request,'Administrator/AdminRegistration.html',{'data':admindata})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'data':admindata})


def delAdmin(request,delID):
    tbl_admin.objects.get(id=delID).delete()
    return redirect("Administrator:adminInsertSelect")
    
def editAdminReg(request,editID):
    ed=tbl_admin.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('txtphone')
        password=request.POST.get('txtpwd')
        ed.admin_name=name
        ed.admin_contact=contact
        ed.admin_email=email
        ed.admin_password=password
        ed.save()
        """save() is the savefunction in django """
        return redirect("Administrator:adminInsertSelect")
    else:
        return render(request,"Administrator/AdminRegistration.html",{'edit':ed})

#District section 
#start from this :
def districtInsertSelect(request):
    districtData = tbl_district.objects.all()
    if request.method=="POST":
        districtName = request.POST.get('txtdist')
        tbl_district.objects.create(district_name = districtName)
        return render(request,'Administrator/District.html',{'districtData':districtData})
    else:
        return render(request,'Administrator/District.html',{'districtData':districtData})

def delDistrict(request,delID):
    tbl_district.objects.get(id=delID).delete()
    return redirect("Administrator:districtInsertSelect")

def editDistrict(request,editID):
    ed=tbl_district.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtdist")
        ed.district_name=name
        ed.save()
        """save() is the savefunction in django """
        return redirect("Administrator:districtInsertSelect")
    else:
        return render(request,"Administrator/District.html",{'edit':ed})
    
    
#Complaint section start from this :    
def ComplaintTypeInsertSelect(request):
    ComplaintTypedata = tbl_complainttype.objects.all()
    if request.method=="POST":
        Complainttypename = request.POST.get('txtname')
        tbl_complainttype.objects.create(complainttype_name = Complainttypename)
        return render(request,'Administrator/ComplaintType.html',{'ComplaintTypedata':ComplaintTypedata})
    else:
        return render(request,'Administrator/ComplaintType.html',{'ComplaintTypedata':ComplaintTypedata})
    
def delcomplainttype(request,delID):
    tbl_complainttype.objects.get(id=delID).delete()
    return redirect("Administrator:ComplaintTypeInsertSelect")

def editcomplainttype(request,editID):
    ed=tbl_complainttype.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtname")
        ed.complainttype_name=name
        ed.save()
        """save() is the savefunction in django """
        return redirect("Administrator:ComplaintTypeInsertSelect")
    else:
        return render(request,"Administrator/ComplaintType.html",{'edit':ed})
    

#Bloodgroup section start from this :
   
def bloodgroupInsertSelect(request):
    blooddata=tbl_bloodgroup.objects.all()
    if request.method=="POST":
        bloodname = request.POST.get('txtname')
        tbl_bloodgroup.objects.create(Bloodgroup_name = bloodname)
        return render(request,'Administrator/Bloodgroup.html',{'blooddata':blooddata})
    else:
        return render(request,'Administrator/Bloodgroup.html',{'blooddata':blooddata})

def delBlood(request,delID):
    tbl_bloodgroup.objects.get(id=delID).delete()
    return redirect("Administrator:bloodgroupInsertSelect")
 
def editBlood(request,editID):
    ed=tbl_bloodgroup.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtname")
        ed.Bloodgroup_name=name
        ed.save()
        return redirect("Administrator:bloodgroupInsertSelect")
    else:
        return render(request,"Administrator/Bloodgroup.html",{'edit':ed})
    


#Place sectiion start from this :
def placeInsertSelect(request):
    placeData=tbl_place.objects.all()
    districtData=tbl_district.objects.all()
    if request.method=="POST":
        placename = request.POST.get('txtplace')
        district=tbl_district.objects.get(id=request.POST.get('selDistrict'))
        tbl_place.objects.create(place_name=placename,district=district)
        return render(request,'Administrator/Place.html',{'placeData':placeData,'districtData':districtData})
    else:
        return render(request,'Administrator/Place.html',{'placeData':placeData,'districtData':districtData})
    
def delplace(request,delID):
    tbl_place.objects.get(id=delID).delete()
    return redirect("Administrator:placeInsertSelect")

def editplace(request,editID):
    districtData=tbl_district.objects.all()
    ed=tbl_place.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtplace")
        ed.place_name=name
        ed.district=tbl_district.objects.get(id=request.POST.get("selDistrict"))
        ed.save()
        return redirect("Administrator:placeInsertSelect")
    else:
        return render(request,"Administrator/Place.html",{'edit':ed,'districtData':districtData})

