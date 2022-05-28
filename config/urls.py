from django.contrib import admin
from django.urls import path

from product.views import *
from account.views import LoginAPIView, LogoutAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ListCreateProductView.as_view(), name='product'),
    path('<int:pk>/', RetrieveProductView.as_view(),),
    path('update/<int:pk>/', UpdateProductView.as_view()),
    path('delete/<int:pk>/', DestroyProductView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]
