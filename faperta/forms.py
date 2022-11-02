from django.forms import ModelForm
from faperta.models import Dosen
from faperta.models import Staff
from faperta.models import Mahasiswa
from django import forms

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'Tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Alamat_Rumah' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
        }

class FormStaff(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

        widgets = {
            'Nama' : forms.NumberInput({'class':'form-control'}),
            'NIP' : forms.TextInput({'class':'form-control'}),
            'Tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Unit' : forms.TextInput({'class':'form-control'}),
            'Alamat_Rumah' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
        }

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'NIM' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'Tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
        }
