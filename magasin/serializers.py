from rest_framework.serializers import ModelSerializer # type: ignore
from magasin.models import Categorie,Produit

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']
class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libelle', 'description', 'categorie']