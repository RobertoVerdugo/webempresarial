from django import forms

class contactoform(forms.Form):
    nombre= forms.CharField(label="Nombre", required=True, widget= forms.TextInput(
        attrs={'class':'form-control'}))
    correo= forms.EmailField(label="Email", required=True, widget= forms.EmailInput(
        attrs={'class':'form-control'}))
    contenido= forms.CharField(label="Mensaje", required=True, widget= forms.Textarea(
        attrs={'class':'form-control', 'rows':3}))