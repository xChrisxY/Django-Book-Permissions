from django.urls import path, include
from .views import LoanViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LoanViewSet, basename='loans')

urlpatterns = [
    path('', include(router.urls))
]
