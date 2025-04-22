from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news_app.views import NewsViewSet, RegisterView, CommentViewSet, LikeViewSet, FavoriteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r"comments", CommentViewSet)
router.register(r'likes', LikeViewSet, basename='likes')
router.register(r'favorites', FavoriteViewSet, basename='favorite')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
