from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
@login_required(login_url='login')
def store(request, category_slug=None):
    products = Product.objects.all()
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    page_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': page_products,
        'product_count': product_count,
    }
    return render(request, "store/store.html", context)

@login_required(login_url='login')
def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }

    return render(request,'store/product_detail.html', context)

def search_product(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count
    }
    return render(request, 'store/store.html', context)
