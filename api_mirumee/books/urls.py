from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/authors', views.AuthorViewV1)
router.register('api/v1/books', views.BooksViewV1)
router.register('api/v1/rates', views.RatesViewV1)

urlpatterns = [
    path('', include(router.urls))
]
