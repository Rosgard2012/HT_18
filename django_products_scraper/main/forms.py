from django import forms

class ProductsAddForm(forms.Form):
    product_ids = forms.CharField(label='Product IDs', max_length=1000)

class ProductDetailForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID')



