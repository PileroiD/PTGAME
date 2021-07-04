from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('game/<slug:slug>/', views.GameDetail.as_view(), name='category'),
    path('category/<slug:slug>/', views.Category.as_view(), name="get_category"),
    path('genre/<slug:slug>/', views.Genre.as_view(), name="get_genre"),
    path('search/', views.Search.as_view(), name='search'),
    path('company/<slug:slug>/', views.Company.as_view(), name='company'),
    path('comment/<int:pk>/', views.AddReview.as_view(), name='comment'),
    # path('like/<int:pk>/', views.LikeView, name='like_game'),
    path('the_most_waiting/', views.MostWaiting.as_view(), name='most_waiting'),
    path('new_games/', views.NewGames.as_view(), name='new_games'),
    path('download_count/<int:pk>/', views.DownloadCount.as_view(), name='count'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
]