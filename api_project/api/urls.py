from django.contrib import admin
from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', view=BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # This includes all routes registered with the router
]


urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
