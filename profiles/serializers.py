from rest_framework import serializers
from .models import Profile,RecipePost


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image'
        ]


class RecipePostSerializer(serializers.ModelSerializer):
    profile_name = serializers.ReadOnlyField(source='owner.profile.name')
    profile_content = serializers.ReadOnlyField(source='owner.profile.content')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = RecipePost
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'title',
            'matter', 'pic'
        ]