from django.views import generic
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    template_name = "products/list_product.html"
    model = Product
    context_object_name = "products"
