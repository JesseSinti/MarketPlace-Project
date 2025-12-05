from django.urls import path 
from . import views
#sets the name used to refer to this specific app in the views and urls
app_name = 'product'
urlpatterns = [
    path('<int:pk>/', views.ProductDetail, name='productdetail'),
    path('newproduct/', views.NewProduct, name='newproduct'),
    path('<int:pk>/delete/', views.DeleteProduct, name='deleteproduct'),
    path('<int:pk>/edit/', views.EditProduct, name='editproduct'),
    path('',views.ProductBrowsing, name='productbrowsing'),
]
