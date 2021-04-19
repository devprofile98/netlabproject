from rest_framework.viewsets import ReadOnlyModelViewSet

from store.api.serializers import ProductSerializers
from store.models import Product, Category

class ProductListViewSet(ReadOnlyModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_queryset(self):
        print(self.kwargs["title"])
        obj = Category.objects.filter(name=self.kwargs["title"])
        if obj.exists():
            return Product.objects.filter(category__name=self.kwargs["title"])
        else:
            return None
        # return Product.objects.all()
