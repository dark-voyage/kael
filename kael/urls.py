from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from kael import redirect
from users import views

admin.site.site_header = "Genemator's API"
admin.site.site_title = "Genemator's Portal"
admin.site.index_title = "Superuser Panel :: Genemator's"

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', redirect.home),
    path('user/', include(router.urls)),
    path('post/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
