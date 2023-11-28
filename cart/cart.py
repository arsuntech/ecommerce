
class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exists
        cart = self.session.get('session_key')

        #If the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        #Make cart available in all web pages
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {
                'name': str(product.name),
                'product_id': product_id,
                'price': str(product.price), 
                'sale_price': str(product.sale_price),
                'is_sale': product.is_sale, 
                'description': str(product.description),
                'image': str(product.image),
                'quantity': quantity
                }
            print(f'this is cart type: {type(self.cart)}')

        self.session.modified = True

    def delete_cart(self, product_id):
        print(f'001{self.cart.keys()} n/ ID: {product_id}')
        del self.cart[product_id]

        print(f'002{self.cart.keys()} n/ ID: {product_id}')

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_cart(self):
        return self.cart