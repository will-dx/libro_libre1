from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['titulo', 'autor', 'descripcion', 'tipo', 'imagen']
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'descripcion': 'Descripción',
            'tipo': 'Tipo de publicación',
            'imagen': 'Imagen de portada',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            ext = imagen.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'webp']:
                raise forms.ValidationError('Formato no permitido. Usa JPG, JPEG, PNG o WEBP.')
        return imagen
