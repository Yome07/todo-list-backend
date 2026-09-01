from rest_framework import serializers

from api.models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=True)
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Le nom de la catégorie ne peut pas être vide")
        if Category.objects.filter(name=value.strip()).exists():
            raise serializers.ValidationError("Cette catégorie existe déjà")
        return value.strip()

class TaskSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=True, allow_blank=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ['id', 'description', 'is_completed', 'category', 'category_id', 'created_at']

    def validate_description(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("La description ne peut pas être vide")
        return value.strip()

    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError("Veuillez sélectionner une catégorie")
        return value