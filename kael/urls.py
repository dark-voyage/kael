from kael import redirect
from django.contrib import admin
from django.urls import path, include
from users.urls import router as users

admin.site.site_header = "Genemator's API"
admin.site.site_title = "Genemator's Portal"
admin.site.index_title = "Superuser Panel :: Genemator's"

urlpatterns = [
    path('', redirect.home),
    path('sudo/', admin.site.urls),
    path('gh/<str:gh>', redirect.github),
    path('user/', include(users.urls)),
    path('post/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
