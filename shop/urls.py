from django.urls import path
from . import views
#from .views import item_list, item_detail, shop_list, shop_detail

app_name = 'shop'

urlpatterns = [
    path('', views.shop_list),
    path('<int:pk>/', views.shop_detail),
    path('item/', views.item_list),
    path('item/<int:pk>/', views.item_detail),
]
