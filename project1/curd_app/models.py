from django.db import models


class Hostel(models.Model):
    NAME_OF_HOSTEL = [("Savitribai Phule", "Savitribai Phule"), ("Regency Hostel", "Regency Hostel"),
    ("Blue Star Hostel", "Blue Star Hostel")]
    CATEGORY = [("OBC", "OBC"), ("SC", "SC"), ("ST", "ST"), ("GEN", "GEN")]
    stu_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    name_of_admitted_course = models.CharField(max_length=30)
    name_of_hostel = models.CharField(max_length=20, choices=NAME_OF_HOSTEL)
    category = models.CharField(max_length=10, choices=CATEGORY)
    date_of_birth = models.DateField()
    father_phone_no = models.IntegerField()
    stu_email = models.EmailField()
