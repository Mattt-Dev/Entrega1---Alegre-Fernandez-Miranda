from django import forms

class crear_formulario_Curso(forms.Form):
    curso = forms.CharField()
    fecha_inicio = forms.DateField()
    profesor = forms.CharField()
    comision = forms.IntegerField()

class crear_formulario_Evento(forms.Form):
    nombre_evento = forms.CharField(max_length=30)
    fecha_inicio = forms.DateField()
    disertante = forms.CharField(max_length=30)

class crear_formulario_Nosotros(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    estudios = forms.CharField(max_length=30)
    acerca_de = forms.CharField(max_length=150)