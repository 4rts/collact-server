from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import verify_jwt_token

from accounts import views
from accounts.views import UserInfoView, UserLoginView, UserRegisterView, UserActivateView, TokenRefreshView

router = DefaultRouter()
router.register('config', views.ConfigViewSet, basename='config')

urlpatterns = [
    path('users/me/', UserInfoView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('users/register', UserRegisterView.as_view()),
    path('users/activate', UserActivateView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', verify_jwt_token),

    path('', include(router.urls)),
]
