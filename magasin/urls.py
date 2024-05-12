from . import views
from django.urls import path
from .views import CategoryAPIView

urlpatterns=[
    path('',views.index,name='index'),
    path('Produits/',views.allProducts,name='allProducts') ,
    path('Fournisseur/',views.Fournisseurs,name='Four') ,
    path('ajoutFournisseur/',views.addProvider,name='ajoutFournisseur') ,
    path('addProduct/',views.addProduct,name='addProduct') ,
    path('commandes/',views.com,name='commandes') ,
    path('mesProduits/',views.mesProduits,name='mesProduits') ,
    path('ajoutCommande/',views.addCommande,name='ajoutCommande'),
    path('delete-product/', views.delete_product, name='delete_product'),
    path('modify_product/', views.modify_product, name='modify_product'),
    path('admin/',views.com,name='admin') ,
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view())

]