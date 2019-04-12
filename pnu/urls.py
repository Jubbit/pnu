from django.contrib import admin
from django.urls import include, path


from django.shortcuts import redirect
def root(request):
    return redirect("/shop/")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', root),
]
