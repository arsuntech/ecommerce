from .cart import Cart

#Create context processor, so cart can work in all pages
def cart(request):
    #Return the default data from Cart
    return {'cart': Cart(request)}
     