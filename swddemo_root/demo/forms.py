from django import forms
from django.forms import ModelForm
from .models import Leave

class LeaveForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Leave
        fields = [
            'name', 'designation', 'leavestart', 'leaveend', 
            'reason'
        ]

class ApprovalForm(forms.Form):
    approval = forms.CharField(max_length=40)

