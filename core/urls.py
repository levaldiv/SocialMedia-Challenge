# This will be my URL routings
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'), # home url
   path('settings', views.settings, name='settings'), # settings url
   path('upload', views.upload, name='upload'), # upload url
   path('follow', views.follow, name='follow'), # follow url
   path('search', views.search, name='search'), # search url
   path('profile/<str:pk>', views.profile, name='profile'), # profile url
   path('like-post', views.like_post, name='like-post'), # like-post url
   path('signup', views.signup, name='signup'), # signup url
   path('signin', views.signin, name='signin'), # signin url
   path('logout', views.logout, name='logout'), # logout url
]
