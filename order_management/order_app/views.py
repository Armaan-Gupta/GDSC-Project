from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     context = {
#         'orders': Order.objects.all()               # used to query the order data from the database
#     }
#     return render(request, 'order_app/home.html', context)

class OrderListView(ListView):
    model = Order
    template_name = 'order_app/home.html'    # the server by default searches for the template of this view in <app>/<model>_<viewtype>.html file
    context_object_name = 'orders'
    ordering = ['-date_placed']

def view_favourites(request):
    favourite = Order.objects.filter(favourites = request.user)
    return render(request, 'order_app/view_favourites.html', {'favourites':favourite})

class OrderDetailView(DetailView):
    model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['title', 'content', 'customer', 'tags']

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['title', 'content', 'customer', 'tags']

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/'

@login_required
def add_favourite(request, id):
    order=get_object_or_404(Order,id=id)
    if order.favourites.filter(id=request.user.id).exists():
        order.favourites.remove(request.user)
    else:
        order.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def search_tags(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_tags = Order.objects.filter(tags__name__icontains=searched)
        return render(request, 'order_app/search_tags.html', {'searched':searched, 'searched_tags':searched_tags})

