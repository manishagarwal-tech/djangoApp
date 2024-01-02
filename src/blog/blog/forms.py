from django import forms

# create forms for contact page
class ContactFrom(forms.Form):
    full_name = forms.CharField()
    email =  forms.EmailField()
    message  = forms.CharField(widget=forms.Textarea)