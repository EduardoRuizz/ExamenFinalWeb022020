from django import forms  
from myapp.models import Producto  


class ProductoForm(forms.ModelForm):  
    precio= forms.FloatField()
    existencia= forms.IntegerField()
    class Meta:  
        model = Producto 
        fields = ['nombre', 'precio', 'existencia', 'descripcion'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'nombre': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'descripcion': forms.Textarea(attrs={ 'class': 'form-control' }),
      }




    


