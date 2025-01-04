from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label="Product Name", max_length=255)
    description = forms.CharField(
        label="Product Description", widget=forms.Textarea, max_length=300
    )
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Product Price")
    available = forms.BooleanField(
        label="Product Availability", initial=True, required=False
    )
    photo = forms.ImageField(label="Product Photo", required=False)

    def save(self):
        print(self.cleaned_data)
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
