from rest_framework.routers import DefaultRouter

from pdv.partners.views import PartnersViewSet

router = DefaultRouter()
router.register(r'partners', PartnersViewSet, basename='partner')
urlpatterns = router.urls
