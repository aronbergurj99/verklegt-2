from datetime import datetime
from shop.models import Product
from django.shortcuts import get_object_or_404

class SearchHistorySession(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        search_history = self.session.get('search-history', False)
        if not search_history:
            search_history = self.session['search-history'] = []
        self.search_history = search_history

    def add_search_history(self, product_id):
        p = get_object_or_404(Product, id=int(product_id))
        product = {
            'id': p.id,
            'name': p.name,
            'price': int(p.price),
            'image': p.productimage_set.first().image.url
        }
        self.search_history.append({"product": product, "datetime": str(datetime.now())})
        self.session['search-history'] = self.search_history
        self.session.modified = True

    def get_history(self):
        h = self.session['search-history']

        return [item['product'] for item in h][::-1]