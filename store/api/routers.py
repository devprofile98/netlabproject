from rest_framework import routers

from store.api.views import ProductListViewSet

router = routers.DefaultRouter()
router.register(r"products/(?P<title>\w+)", ProductListViewSet, basename="products")