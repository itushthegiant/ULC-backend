from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet)
router.register('properties', views.PropertyViewSet)
router.register('units', views.UnitViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
