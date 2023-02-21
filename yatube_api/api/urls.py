from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GrouptViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/groups', GrouptViewSet)
router_v1.register(r'^v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register('v1/follow', FollowViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
