from django.urls import path
from .views import post_list, post_detail, PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>-<int:month>-<int:day>/<slug:slug>/', post_detail, name='post_detail'),
    path('id/<int:id>/', post_detail, name='post_detail')
]