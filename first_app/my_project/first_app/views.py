from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def my_view(request):
    return render(request, "first_app/car_list.html", context)


class CarListView(TemplateView):
    template_name = "first_app/car_list.html"

    def get_context_data(self, **kwargs):
        cart_list = [
            {"title": "Toyota"},
            {"title": "BMW"},
        ]

        return {"car_list": cart_list}


def my_test_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return HttpResponse("Hello, World!")
