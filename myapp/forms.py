from django import forms
from .models import Post
from .models import Doctor
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('name', 'phone_number', 'work_experience', 'qualification', 'department')

class DeleteDoctorForm(forms.Form):
    name = forms.CharField(max_length = 100)
