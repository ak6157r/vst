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
        fields = ('iccid1','msisdn1','status')
        widgets = {
            'iccid1': forms.TextInput(attrs={'class':'form-control'}),
            'msisdn1'  : forms.TextInput(attrs={'class':'form-control'}),
            'status'  : forms.Select(attrs={'class':'form-control'}),
        }
        
class Branch2Form(forms.ModelForm):
    class Meta:
        model = Branch2
        fields = ('iccid2','msisdn2','status')
        widgets = {
            'iccid2': forms.TextInput(attrs={'class':'form-control'}),
            'msisdn2': forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
        }
        
class Branch3Form(forms.ModelForm):
    class Meta:
        model = Branch3
        fields = ('iccid1','imei','serial','status')
        widgets = {
            'iccid1': forms.TextInput(attrs={'class':'form-control'}),
            'imei': forms.TextInput(attrs={'class':'form-control'}),
            'serial': forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
        }
        
    