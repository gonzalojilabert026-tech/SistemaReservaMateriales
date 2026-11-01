from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = '__all__'

    def clean_stock(self):
        stock = self.cleaned_data['stock']

        if stock < 0:
            raise forms.ValidationError(
                'El stock no puede ser negativo.'
            )

        return stock

    def clean_precio_referencia(self):
        precio = self.cleaned_data['precio_referencia']

        if precio < 0:
            raise forms.ValidationError(
                'El precio no puede ser negativo.'
            )

        return precio