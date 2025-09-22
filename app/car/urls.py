from rest_framework.routers import DefaultRouter
from app.car.views import CArViewsetsAPI, CarViewSet, CategoryViewSet

router = DefaultRouter()
router.register('car', CArViewsetsAPI, basename='car')  
router.register('cars', CarViewSet, basename='car')       
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = router.urls
