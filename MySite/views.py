from django.shortcuts import render 
from django.template import loader 
from django.contrib.auth.decorators import login_required
from magasin.models import Produit, Categorie
from magasin.serializers import CategorySerializer, ProduitSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import status, viewsets # type: ignore
from rest_framework.views import APIView # type: ignore
@login_required
def index(request):
    return render(request,'acceuil.html' ) 





class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProduitAPIView(APIView):
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
