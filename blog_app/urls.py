from django.urls import path
from .views import PostListView, post_detail, post_share

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post-detail'),
    path('<int:post_id>/share/', post_share, name='post-share'),
]
