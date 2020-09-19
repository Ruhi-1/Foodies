from django.shortcuts import render
# from .models import Category, Product
# from cart.forms import CartAddProductForm


def index(request):
    return render(request,'foodiesapp/index.html')

# def index_contact(request):
#     return render(request,'foodiesapp/index.html')

def breakfast(request):
    return render(request, 'foodiesapp/breakfast.html')

def lunch(request):
    return render(request, 'foodiesapp/lunch.html')

def burger(request):
    return render(request, 'foodiesapp/burger.html')

def kolaches(request):
    return render(request, 'foodiesapp/kolaches.html')

def cookies(request):
    return render(request, 'foodiesapp/cookies.html')

def bread(request):
    return render(request, 'foodiesapp/bread.html')

def gelato(request):
    return render(request, 'foodiesapp/gelato.html')

def coffee(request):
    return render(request, 'foodiesapp/coffee.html')

def about(request):
    return render(request, 'foodiesapp/about.html')


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.object.all()
#     products = Product.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'foodiesapp/product/list.html', {'category': category,
#                                                       'categories': categories,
#                                                       'products': products})

# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request,
#                   'foodiesapp/product/detail.html',
#                   ('product': product,
#                   'cart_product_form': cart_product_form))
