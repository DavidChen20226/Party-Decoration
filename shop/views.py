from django.shortcuts import render, get_object_or_404
from .models import Category, Product 
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q 
# Create your views here. 
def prod_list(request, category_id=None): 
    category = None 
    products = Product.objects.filter(available=True) 
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True) 
    
    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('Page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage): 
        products = paginator.page(paginator.num_page)
    
    return  render(request, 'shop/category.html',{'category':category, 'prods':products}) 
    
def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'shop/product.html', {'product':product})

def filterView(request): 
    Price_Low = request.GET.get('PriceLow')
    Price_High = request.GET.get('PriceHigh')