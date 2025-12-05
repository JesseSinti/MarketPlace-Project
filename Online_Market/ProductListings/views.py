from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import NewProductForm, EditProductForm
# Create your views here.

# use pk intead of id pk == id but stops potential problems
# request.user returns the user who is logged in on their session
# in the returns/renders product refers to the app and products refers to the folder holding the html(for includes in main urls.py)

def ProductDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    #.exlcude keeps the item selected from popping up as a related item and [0:3] tells how many items to show as related
    similarProduct = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'products/ProductDetail.html', {'product' : product, 'related_product': similarProduct})

@login_required
def NewProduct(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product:productdetail',pk=product.id)
    else:
        form = NewProductForm()
    return render(request,'products/NewProduct.html', {'form':form})

@login_required
def DeleteProduct(request,pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    product.delete()
    return redirect('dashboard:UserHome')

@login_required
def EditProduct(request, pk):
    product = get_object_or_404(Product,pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product:productdetail', pk=product.id)
    else:
        form = EditProductForm(instance=product)
    return render(request, 'products/NewProduct.html', {'form' : form, 'title' : 'Edit Product'})

def ProductBrowsing(request):
    items_queryset = Product.objects.filter(is_sold=False)
    cat_id = request.GET.get('category')
    
    view_selected_category = None
    all_categories = Category.objects.all()

    if cat_id:
        items_queryset = items_queryset.filter(category_id=cat_id)
        view_selected_category = Category.objects.filter(id=cat_id).first()
    
    context = {
    'filtered_items': items_queryset,
    'view_selected_category': view_selected_category,
    'all_categories': all_categories,
    'global_categories': all_categories,
    'global_selected_category': view_selected_category,
    }
    return render(request, 'storefront/home.html', context)