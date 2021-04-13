from django.urls import path, include
from .views import IndexView, OrderListView, OrderCreateView, CommissionListView,CommissionCreateView ,ReferenceListView, ReferenceCreateView

urlpatterns = [
    path('',IndexView, name='index')
]
