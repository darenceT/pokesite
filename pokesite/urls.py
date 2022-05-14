from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'character', views.CharacterViewSet)

urlpatterns = [
    path("", views.index, name='index'),
    path("sections/<int:num>", views.section, name='section'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]