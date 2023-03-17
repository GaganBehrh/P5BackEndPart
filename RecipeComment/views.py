from django.shortcuts import render

from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RecipeComment
from .serializers import RecipeCommentSerializer
from p5django.permissions import IsOwnerOrReadOnly


class RecipeCommentList(APIView):
    serializer_class = RecipeCommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        recipecomments = RecipeComment.objects.all()
        serializer = RecipeCommentSerializer(
            recipecomments, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeCommentSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class RecipeCommentDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeCommentSerializer

    def get_object(self, pk):
        try:
            recipecomment = RecipeComment.objects.get(pk=pk)
            self.check_object_permissions(self.request, recipecomment)
            return recipecomment
        except RecipeComment().DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipecomment = self.get_object(pk)
        serializer = RecipeCommentSerializer(
            recipecomment, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        recipecomment = self.get_object(pk)
        serializer = RecipeCommentSerializer(
            recipecomment, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        recipecomment = self.get_object(pk)
        recipecomment.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
