from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ProductListings.models import *
from .forms import *
from django.db.models import Q
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def CheckoutView(request, pk):
    product = Product.objects.get(id=pk)
    image_url = None
    if product.image:
        image_url = request.build_absolute_uri(product.image.url)
    print (image_url)
    MY_DOMAIN = f"{request.scheme}://{request.get_host()}"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency':'usd',
                'unit_amount':int(product.price * 100),
                'product_data': {
                    "name":product.name,
                    'images':[image_url] if image_url else [],
                },
            },
            'quantity':1,
        },
    ],
    metadata = {
        'product_id':pk,
        'user_email':request.user.email
    },
    mode='payment',
    success_url=MY_DOMAIN + f'/payment-success/{pk}',
    cancel_url=MY_DOMAIN + f'/pricing/{pk}',
    )
    return redirect(checkout_session.url)

def Log_out(request):
    logout(request)
    return redirect('/storefront/login/')

def StoreFrontHome(request):
    UnsoldProducts = Product.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'storefront/home', {'categories' : categories, 'products' : UnsoldProducts})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/storefront/login/')
    else:
        form = SignupForm()
    return render(request, 'storefront/signup.html', {'form' : form})

def SearchProducts(request):
    query = request.GET.get('query', '')
    category = Category.objects.all()
    products = Product.objects.filter(is_sold=False)

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

        return render(request, 'storefront/search.html', {'products' :products, 'query' : query, 'category' : category})
    

@login_required
def UserCart(request):
    products = Product.objects.filter()
    return render(request, 'usercart.html', {'products' : products})