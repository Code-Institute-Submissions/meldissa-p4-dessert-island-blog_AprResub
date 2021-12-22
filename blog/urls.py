from . import views
from django.urls import path

"""
Please note code was used from the Code Institute I Think Therefore I Blog
tutorial to help create this project.
"""

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
