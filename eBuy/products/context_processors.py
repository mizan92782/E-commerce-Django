# shop/context_processors.py

from .models import product_category

def category_context(request):
    categories = [cat[0] for cat in product_category]
    return {
        'categorieslist': categories
    }