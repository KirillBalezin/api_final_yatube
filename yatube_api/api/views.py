from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from .serializers import (PostSerializer, CommentSerializer,
                          GroupSerializer, FollowSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GrouptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)

    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        )


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
