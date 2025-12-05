from ProductListings.models import Category
from django.db.models import Count, Q

def global_categories(request):
    categories_with_products = Category.objects.annotate(
        num_items = Count(
            'products',
            filter=Q(products__is_sold=False)
        )
    ).filter(num_items__gt=0)

    selected_category = None
    category_id = request.GET.get('category')

    if category_id and category_id.isdigit():
        try:
            selected_category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            pass

    return {
        'global_categories' : categories_with_products,
        'global_selected_category' : selected_category
    }