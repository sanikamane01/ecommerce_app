
from django.contrib import admin
from django.urls import path
from shopping import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('create-product/', views.create_product, name='create_product'),
    path('get-products/', views.get_products,name='get_products'),
    path('update-product/',views.update_product,name='update_product'),
    path('delete-product/',views.delete_product,name='delete_product'),
    path('search-products/',views.search_products,name='search_products'),

    # user urls
    path('login/', user_views.login, name='login'),
    path('register/', user_views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)