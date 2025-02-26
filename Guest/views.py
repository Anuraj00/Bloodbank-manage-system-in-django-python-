from django.shortcuts import render
from Guest.models import *
from Administrator.models import *

# Create your views here.

#for the donor registration : 

def donorInsert(request):
    data=tbl_district.objects.all()


    blooddata=tbl_bloodgroup.objects.all()

    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        age=request.POST.get('txtage')
        contact=request.POST.get('txtphone')
        address=request.POST.get('txtname')
        photo=request.FILES.get('filePhoto')
        bloodgroup=request.POST.get('selBloodgroup')
        disease=request.POST.get('txtdise')
        password=request.POST.get('txtpwd')


        bloodgroup=tbl_bloodgroup.objects.get(id=request.POST.get('selBloodgroup'))
        
        place=tbl_place.objects.get(id=request.POST.get('selPlace'))

        tbl_donor.objects.create(place=place,bloodgroup=bloodgroup,donor_name=name,
                                 donor_contact=contact,donor_email=email,donor_password=password,donor_address=address,
                                 donor_photo=photo,disease_status=disease,donor_age=age)
        return render(request,'Guest/DonorRegistration.html',{'data':data,'blooddata':blooddata})
    else:
        return render(request,'Guest/DonorRegistration.html',{'data':data,'blooddata':blooddata})
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})