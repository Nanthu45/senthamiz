from django.shortcuts import render
from django.http import HttpResponse
from core.models import Category,Product,ProductImages
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def index(request, cid=None):
    categories = Category.objects.all()  
    if cid:
        category = get_object_or_404(Category, id=cid)
        products = Product.objects.filter(product_status="published", featured=True, Category=category).order_by("-id")
    else:
        products = Product.objects.filter(product_status="published", featured=True).order_by("-id")
        category = None
    username = request.user.username
    context = {
        "products": products,
        "categories": categories, 
        "category": category,
        "is_authenticated": request.user.is_authenticated,  
        "username": username,
    }
    return render(request, 'core/index.html', context)

def product(request, cid=None):
    if cid:
        category = get_object_or_404(Category, id=cid)
        products = Product.objects.filter(product_status="published", Category=category).order_by("-id")
    else:
        products = Product.objects.filter(product_status="published").order_by("-id")
        category = None
    
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    is_authenticated = request.user.is_authenticated
    can_view_products = request.user.can_view_products if is_authenticated else False
    username = request.user.username
    
    context = {
        "page_obj": page_obj,
        "category": category,
        "is_authenticated": is_authenticated,
        "view": can_view_products,
        "username": username,
    }
    
    return render(request, 'core/product.html', context)

def product_details(request,pid):
    product=Product.objects.get(pid=pid)
    p_image = product.p_images.all()
    special_features = product.special_features.split(',') if product.special_features else []
    products = Product.objects.filter(Category=product.Category)
    username = request.user.username
    is_authenticated = request.user.is_authenticated
    context = {
        "p":product,
        "p_images":p_image,
        "special_features": special_features, 
        'latitude': product.latitude if product else None,  
        'longitude': product.longitude if product else None, 
        "products": products,
        "username": username,
        "is_authenticated": is_authenticated,
    }
    return render (request,'core/Products_Details.html',context)


def login(request):
    return render (request,'core/login.html')




     