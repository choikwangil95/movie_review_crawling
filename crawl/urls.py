from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('reviewlist/', views.ReviewList.as_view(), name = 'reviewlist'),
    path('', views.HomeView.as_view(), name = 'homeview')
]