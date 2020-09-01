from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('authors', views.AuthorView)
router.register('books', views.BooksView)
router.register('rates', views.RatesView)

urlpatterns = [
    path('', include(router.urls))
]
