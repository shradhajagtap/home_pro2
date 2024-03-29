from django import forms

from .models import Hostel


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = "__all__"

        widgets = {
            "stu_name": forms.TextInput(attrs={"class": "form-control"}),
            "father_name": forms.TextInput(attrs={"class": "form-control"}),
            "mother_name": forms.TextInput(attrs={"class": "form-control"}),
            "name_of_admitted_course": forms.TextInput(attrs={"class": "form-control"}),
            "name_of_hostel": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(),
            "father_phone_no": forms.NumberInput(),
            "stu_email": forms.EmailInput()
        }
