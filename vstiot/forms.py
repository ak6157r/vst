from django import forms
from . models import Items
from . models import Branch1, Branch2, Branch3

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        widgets = {
            'ICCID1': forms.TextInput(attrs={'class':'form-control'}),
            'IMSI1' : forms.TextInput(attrs={'class':'form-control'}),
            'MSISDN1' : forms.TextInput(attrs={'class':'form-control'}),
            'ICCID2' : forms.TextInput(attrs={'class':'form-control'}),
            'IMSI2' : forms.TextInput(attrs={'class':'form-control'}),
            'MSISDN2' : forms.TextInput(attrs={'class':'form-control'}),
            'IMEI' : forms.TextInput(attrs={'class':'form-control'}),
            'STATUS' : forms.Select(attrs={'class':'form-control'}),
        }

class Branch1Form(forms.ModelForm):
    class Meta:
        model = Branch1
        fields = ('ICCID1','MSISDN1','STATUS')
        widgets = {
            'ICCID1': forms.TextInput(attrs={'class':'form-control'}),
            'MSISDN1'  : forms.TextInput(attrs={'class':'form-control'}),
            'STATUS'  : forms.Select(attrs={'class':'form-control'}),
        }
        
class Branch2Form(forms.ModelForm):
    class Meta:
        model = Branch2
        fields = ('ICCID2','MSISDN2','STATUS')
        widgets = {
            'ICCID2': forms.TextInput(attrs={'class':'form-control'}),
            'MSISDN2': forms.TextInput(attrs={'class':'form-control'}),
            'STATUS' : forms.Select(attrs={'class':'form-control'}),
        }
        
class Branch3Form(forms.ModelForm):
    class Meta:
        model = Branch3
        fields = ('ICCID1','IMEI','SERIAL','STATUS')
        widgets = {
            'ICCID1': forms.TextInput(attrs={'class':'form-control'}),
            'IMEI': forms.TextInput(attrs={'class':'form-control'}),
            'SERIAL': forms.TextInput(attrs={'class':'form-control'}),
            'STATUS' : forms.Select(attrs={'class':'form-control'}),
        }
        
    