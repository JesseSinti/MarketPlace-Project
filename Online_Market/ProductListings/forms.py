from django import forms

from .models import Product
#styles the textboxes
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewProductForm(forms.ModelForm):
    class Meta:
        #sets the form to add the 'product' to this model
        model = Product
        fields = ('category','name','description','price','image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class EditProductForm(forms.ModelForm):
    class Meta: 
        #sets the form to edit the 'product' in this model
        model = Product 
        fields = ('name', 'description','price','image','is_sold')
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description' : forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price' : forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            })
        }