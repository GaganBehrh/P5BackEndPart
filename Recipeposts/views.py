from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RecipePost
from .serializers import RecipePostSerializer
from p5django.permissions import IsOwnerOrReadOnly


class RecipePostList(APIView):
    serializer_class = RecipePostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        recipeposts = RecipePost.objects.all()
        serializer = RecipePostSerializer(
            recipeposts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipePostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class RecipePostDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipePostSerializer

    def get_object(self, pk):
        try:
            post = RecipePost.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except RecipePost().DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = RecipePostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = RecipePostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
