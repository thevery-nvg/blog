from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', ByCategory.as_view(), name='category'),
    path('post/<int:year>/<int:month>/<int:day>/<str:slug>/', PostView.as_view(), name='post'),
    path('tag/<str:slug>/', ByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
    path('addpost/', AddPost.as_view(), name='post_add'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/edit', UpdatePost.as_view(), name='post_update'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/delete/', DeletePost.as_view(), name='post_delete'),
]
