from django.urls import include, path
#어떤 경로로 요청하고 경로로 받을지 정함
from rest_framework.routers import DefaultRouter 
from . import views

router = DefaultRouter()
router.register('myapp',views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

]


