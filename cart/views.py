from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    #cart_item = Session.objects.all()
    #cart_item = cart_item[2].get_decoded()['session_key'].values()
    cart = Cart(request)
    cart_item = cart.get_cart().values()
    cart_item = reversed(cart_item)
    return render(request, 'cart_summary.html', {'cart_item': cart_item})

def cart_add(request):
    #Get cart
    cart = Cart(request)
    #test POST
    if request.POST.get('action') == 'post':
        #get product
        product_id = int(request.POST.get('product_id'))
        quantity = request.POST.get('quantity')
        if not quantity:
            quantity = 1
            
        print(f'Product quantity: {quantity}')

        #lookup product in DB
        product = get_object_or_404(Product, id = product_id)

        #Save to session
        cart.add(product = product, quantity = quantity)

        cart_quantity = cart.__len__()

        #return response
        response = JsonResponse({'cart_quantity': cart_quantity})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        del_pro_id = request.POST.get('del_pro_id')
        print(f'this s the cureent id in chop {del_pro_id} ^ {type(del_pro_id)}')
        cart.delete_cart(product_id = del_pro_id)
        cart_quantity = cart.__len__()
        
        

        #return response
        response = JsonResponse({'cart_quantity': cart_quantity})
        return response


def cart_update(request):
    pass