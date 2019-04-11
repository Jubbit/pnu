from django.urls import path
from .views import item_list, item_detail

app_name = 'shop'

urlpatterns = [
    path('', item_list),
    path('<int:pk>/', item_detail),
    #int형태를 받아서 views-item_detail 함수의 pk에 던져준다.
]