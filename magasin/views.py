from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from magasin.forms import FournisseurForm, ProduitForm, CommandeForm, UserRegistrationForm
from magasin.models import Fournisseur, Produit, Commande, Categorie
from magasin.serializers import CategorySerializer, ProduitSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import status, viewsets # type: ignore
from rest_framework.views import APIView # type: ignore

def index(request):
    return redirect('allProducts')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hello {username}, Your account has been created successfully!')
            return redirect('index')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

def addProvider(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Four')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/ajoutFournisseur.html', {'form': form})

def allProducts(request):
    list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})

def Fournisseurs(request):
    liste = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'liste': liste})

def addProduct(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('allProducts')
    else:
        form = ProduitForm()
    return render(request, 'magasin/majProduits.html', {'form': form})

def com(request):
    commandes = Commande.objects.all()
    return render(request, 'magasin/commande.html', {'commandes': commandes})

def addCommande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('commandes')
    else:
        form = CommandeForm()
        return render(request, 'magasin/ajoutCommande.html', {'form': form})

def mesProduits(request):
    if request.method == "GET":
        libelle_param = request.GET.get('libellé')
        if libelle_param:
            list = Produit.objects.filter(libellé=libelle_param.capitalize())
            return render(request, 'magasin/mesProduits.html', {'list': list})
        
    list = Produit.objects.all()
    return render(request, 'magasin/mesProduits.html', {'list': list})

def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        Produit.objects.filter(id=product_id).delete()
        return redirect('mesProduits')
    return redirect('mesProduits')

def modify_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        modified_name = request.POST.get('modified_name')
        modified_description = request.POST.get('modified_description')
        modified_price = request.POST.get('modified_price')
        
        product = Produit.objects.get(id=product_id)
        product.libellé = modified_name
        product.description = modified_description
        product.prix = modified_price
        product.save()
        
        return redirect('mesProduits')

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
