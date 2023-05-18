from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.CharField()
    mensaje = forms.CharField()