from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ProductListings.models import Product
# Create your views here.
@login_required
def UserHome(request):
    products = Product.objects.filter(created_by=request.user)
    return render(request, 'dashboard/UserHome.html', {'products' : products})