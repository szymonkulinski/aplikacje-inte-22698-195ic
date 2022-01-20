from django.urls import path,include,re_path
from .views import UserList, UserDetail
#UserViewSet, PostViewSet
from .views import  PostList, PostDetail
from . import views


urlpatterns = [
    re_path('users/', UserList.as_view()),
    re_path('users/<int:pk>/', UserDetail.as_view()), 
    re_path('<int:pk>/', PostDetail.as_view()),
    #path('', views.PostList),
    re_path('', PostList.as_view()),
    #path('a', views.setcookie, name='test_cookie'),
]
