from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from magasin.views import ProductViewset,CategoryAPIView,index
from rest_framework import routers # type: ignore
from .views import CategoryAPIView, ProductViewset


# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin',include('magasin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view(), name='category_api'), 
    path('api/produits/', ProductViewset.as_view({'get': 'list', 'post': 'create'}), name='produit_api'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
