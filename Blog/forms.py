from django import forms

class PostFormulario(forms.Form):
    autor = forms.CharField(max_length=200)
    titulo= forms.CharField(max_length=200)
    resumen = forms.CharField(max_length=500)
    contenido = forms.CharField()
    imagen = forms.CharField(max_length=200)
    fecha = forms.DateTimeField()
    categoria = forms.CharField(max_length=200)