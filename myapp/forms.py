from django.forms.extras.widgets import SelectDateWidget
from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            'name',
            'phone_number',
            'work_experience',
            'qualification',
            'department'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'ФИО врача','class':'form-control'}),
            'birth_date': SelectDateWidget(years=range(1920, 2100)),
            'phone_number':forms.TextInput(attrs={'placeholder':'Номер телефона','class':'form-control'}),
            'work_experience':forms.TextInput(attrs={'placeholder':'Опыт работы','class':'form-control'}),
        }
        labels = {
            'name' : 'Имя',
            'phone_number': 'Номер телефона',
            'work_experience': 'Опыт работы',
            'qualification' : 'Квалификация',
            'department': 'Отделение',
        }
class NurseForm(forms.ModelForm):

    class Meta:
        model = Nurse
        fields = [
            'name',
            'phone_number',
            'work_experience',
            'department'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'ФИО медсестры','class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'placeholder':'Номер телефона','class':'form-control'}),
            'work_experience':forms.TextInput(attrs={'placeholder':'Опыт работы','class':'form-control'}),
        }
        labels = {
            'name' : 'Имя',
            'phone_number': 'Номер телефона',
            'work_experience': 'Опыт работы',
            'qualification' : 'Квалификация',
            'department': 'Отделение',
        }
class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', )
        enter_date = forms.DateField()

        fields = [
            'name',
            'history_number',
            'enter_date'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'ФИО пациента','class':'form-control'}),
            'history_number':forms.TextInput(attrs={'placeholder':'Номер истории болезни','class':'form-control'}),
            'enter_date': SelectDateWidget(years=range(2010, 2100)),
        }
        labels = {
            'name' : 'Имя',
            'phone_number': 'Номер телефона',
            'history_number': 'Номер истории болезни',
            'enter_date' : 'Дата поступления',
        }

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = [
            'history_number',
            'name',
            'birth_date',
            'department',
            'attending_doctor',
            'diagnosis',
            'ward',
            'destination'
        ]
        widgets = {
            'history_number' : forms.TextInput(attrs={'placeholder':'Номер истории болезни','class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'ФИО пациента','class':'form-control'}),
            'birth_date': SelectDateWidget(years=range(1920, 2100)),
            'attending_doctor':forms.TextInput(attrs={'placeholder':'Лечащий врач','class':'form-control'}),
            'diagnosis':forms.TextInput(attrs={'placeholder':'Диагноз','class':'form-control'}),
            'ward':forms.TextInput(attrs={'placeholder':'Номер палаты','class':'form-control'}),
            'destination':forms.TextInput(attrs={'placeholder':'Назначение врача','class':'form-control'}),
        }
        labels = {
            'history_number':'Номер истории',
            'name' : 'Имя',
            'birth_date': 'Дата рождения',
            'department': 'Отделение',
            'attending_doctor': 'Лечащий врач',
            'diagnosis' : 'Диагноз',
            'ward': 'Палата',
            'destination':'Назначение'
        }
class DeleteDoctorForm(forms.Form):
    name = forms.CharField(max_length = 100)
