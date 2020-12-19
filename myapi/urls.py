from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('addnew', views.addnew, name='addnew'),
    path('api', include(router.urls)),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]