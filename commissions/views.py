from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission, Comment

class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commission_detail.html'
# Create your views here.
