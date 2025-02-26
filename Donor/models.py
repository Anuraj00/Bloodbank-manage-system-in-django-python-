from django.db import models
from Guest.models import *
from Administrator.models import *

# Create your models here.

class tbl_complaint(models.Model):
    complaint_date=models.CharField(max_length=50)
    complaint_status=models.CharField(max_length=50)
    complaint_reply=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    donor_id=models.ForeignKey(tbl_donor,on_delete=models.CASCADE)
    patient_id=models.ForeignKey(tbl_patient,on_delete=models.CASCADE)
    bloodgroup_id=models.ForeignKey(tbl_bloodgroup,on_delete=models.CASCADE)


class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)

class tbl_blooddonate(models.Model):
    blooddonate_unit=models.CharField(max_length=50)
    blooddonate_date=models.CharField(max_length=50)
    donor_id=models.ForeignKey(tbl_donor,on_delete=models.CASCADE)
    bloodgroup_id=models.ForeignKey(tbl_bloodgroup,on_delete=models.CASCADE)
    bloodbank_id=models.ForeignKey(tbl_bloodbank,on_delete=models.CASCADE)


