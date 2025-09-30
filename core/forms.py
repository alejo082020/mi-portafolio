from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'telefono', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com',
                'required': True
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 300 123 4567'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto del mensaje',
                'required': True
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 5,
                'required': True
            })
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if len(mensaje) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres')
        return mensaje
