from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from magasin.models import Produit, Categorie
from magasin.serializers import CategorySerializer, ProduitSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import status, viewsets # type: ignore
from rest_framework.views import APIView # type: ignore

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Template pour afficher la liste des posts
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'  # Template pour créer un nouveau post
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')  # Redirection après création réussie

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_form.html'  # Template pour mettre à jour un post existant
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')  # Redirection après mise à jour réussie

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'  # Template pour confirmer la suppression d'un post
    success_url = reverse_lazy('post_list')  # Redirection après suppression réussie




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

class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
