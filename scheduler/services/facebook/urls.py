from django.urls import path, include

from facebook_login import callback

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('facebook/callback', include(callback))
]