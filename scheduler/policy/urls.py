from django.urls import path
from . import views

urlpatterns = [
    path('privacy_policy', views.privacy_policy),
    path('data_deletion', views.data_deletion),
    path('terms_service', views.terms_service),

]