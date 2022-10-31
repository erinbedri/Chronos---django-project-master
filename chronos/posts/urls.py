from django.urls import path

from chronos.posts import views

urlpatterns = [
    # path('all/', views.show_posts, name='show_posts'),

    path('details/<int:pk>', views.show_post, name='show_post'),
    path('all/', views.PostListView.as_view(), name='show_posts'),
]