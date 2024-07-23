from django import forms
from .models import Work

class WorkCreateForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'image']


class WorkUpdateForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'image']


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=255)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)