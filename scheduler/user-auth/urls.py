from django.urls import path
from . import views

urlpatterns = [
    path('post_posts', views.post_posts),
    path('fetch_posts', views.get_posts),
    path('fetch_post/<pk>', views.get_post),
    path('delete_post/<pk>', views.delete_post),
    path('edit_post/<pk>', views.edit_post),
    path('search_for_a_post', views.search_for_a_post)

]