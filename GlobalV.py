from store.models import Category
#from django.contrib.sessions.models import Session


def get_categories():
    categories = Category.objects.all()
    return categories

'''def get_cart():
    cart_item = Session.objects.all()
    try:
        cart_item = cart_item[1].get_decoded()['session_key'].values()
    except IndexError:
        cart_item = {}
    return cart_item
'''