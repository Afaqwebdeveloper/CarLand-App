from django.urls import path
from . import views

app_name="CarLand"

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('ads/', views.ad_list, name='ad_list'),
    path('ads/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('post_ad/', views.post_ad, name='post_ad'),
    path('filter_ads/', views.filter_ads, name='filter_ads'),
    path('sort_ads/', views.sort_ads, name='sort_ads'),
]
