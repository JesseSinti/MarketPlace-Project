from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
from ProductListings import views as product_views

app_name = 'storefront'
urlpatterns = [
    path('logout/', views.Log_out, name='logout'),
    path('checkout/<int:pk>/', views.CheckoutView, name='checkout'),
    path('search/',views.SearchProducts, name='search'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='storefront/login.html', authentication_form=LoginForm), name='login')
]