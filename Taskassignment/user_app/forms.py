from django import forms

class fileform(forms.Form):
    user_image = forms.FileField()

