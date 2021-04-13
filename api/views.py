from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Order, Commission, Reference

def IndexView(request):
    context = {
        'orders': Order.objects.all(),
        'commissions': Commission,
        'references': Reference

    }
    return render(request, 'index.html', context)

# Create your views here.
class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'home.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'



class CommissionListView(ListView):
    model = Commission
    context_object_name = 'commission_list'
    template_name = 'home.html'

class CommissionCreateView(CreateView):
    model = Commission
    template_name = 'commission_create.html'
    

class ReferenceListView(ListView):
    model = Reference
    context_object_name = 'reference_list'
    template_name = 'home.html'


class ReferenceCreateView(CreateView):
    model = Reference
    template_name = 'reference_create.html'
