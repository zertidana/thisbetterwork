from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Comment, News, Category



class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['ProfileImage', 'Email', 'DoB', 'Favourite']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__' 

class RecursiveSerializer(serializers.Serializer):
    """
    This serializer is used to handle recursive comments (replies).
    """
    def to_representation(self, value):
        serializer = CommentSerializer(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'news', 'name', 'email', 'comment', 'add_time', 'status', 'parent', 'replies']
        extra_kwargs = {
            'parent': {'write_only': True}  # Parent field is write-only
        }

    def create(self, validated_data):
        """
        Custom create method to handle comment creation.
        """
        # Extract the parent comment if it exists
        parent = validated_data.pop('parent', None)
        comment = Comment.objects.create(**validated_data)

        # Link this comment to its parent if it's a reply
        if parent is not None:
            comment.parent = parent
            comment.save()

        return comment