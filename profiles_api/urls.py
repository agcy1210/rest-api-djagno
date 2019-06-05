from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
#router.register({name of API}, {viewset}, views.HelloViewSet)
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)),
    #router automatically generates urls for us
]
