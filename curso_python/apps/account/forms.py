from django import forms
from .models import Move
from .models import MoveLine


class MoveLineForm(forms.ModelForm):
    class Meta:
        model = MoveLine
        fields = ['product', 'detail', 'qty', 'price', 'subtotal']
        labels = {
            # 'move_factura': 'Factura',
            'product': 'Producto',
            'detail': 'Detalle',
            'qty': 'Cantidad',
            'price': 'Precio',
            'subtotal': 'Subtotal',
        }
        widgets = {
            # 'move_factura': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
        }


MoveLineFormSet = forms.inlineformset_factory(Move, MoveLine, form=MoveLineForm, extra=1, can_delete=True)


class MoveForm(forms.ModelForm):
    class Meta:
        model = Move
        fields = ['name', 'cliente', 'date', 'numero_documento', 'total']
        labels = {
            'name': 'Nombre',
            'cliente': 'Cliente',
            'date': 'Fecha',
            'numero_documento': 'Número de documento',
            'total': 'Total',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
