from django.urls import path
from .views import (OrderListView, 
                    OrderDetailView, 
                    OrderCreateView, 
                    OrderUpdateView,
                    OrderDeleteView,)
from . import views

urlpatterns = [
    path('', OrderListView.as_view(), name = 'order_app-home'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name = 'order-detail'),
    path('order/new/', OrderCreateView.as_view(), name = 'order-create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name = 'order-update'),
    path('updated/<int:id>/', views.add_favourite, name = 'order-favourites'),
    path('order/view_favourites/', views.view_favourites, name = 'order-view_favourites'),
    path('order/search_tags/', views.search_tags, name = 'search-tags'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name = 'order-delete'),
]