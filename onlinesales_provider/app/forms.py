from .models import merchantModel,ProductModel
from django import forms

class MerchantForm(forms.ModelForm):
    class Meta:
        model = merchantModel
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'