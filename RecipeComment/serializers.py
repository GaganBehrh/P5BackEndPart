from rest_framework import serializers
from RecipeComment.models import RecipeComment


class RecipeCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    def validate_pic(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.pic.height > 4096:
            raise serializers.ValidationError(
                'Picture height larger than 4096px!'
            )
        if value.pic.width > 4096:
            raise serializers.ValidationError(
                'Picture width larger than 4096px!'
            )
        return value

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = RecipeComment
        fields = [
            'id', 'user', 'is_user', 'profile_id',
            'profile_image', 'comment_created', 'comment_updated',
            'name', 'subject', 'picture'
        ]