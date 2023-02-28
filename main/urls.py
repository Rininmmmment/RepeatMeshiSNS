from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/', views.timeline, name='timeline'),
    path('create/', views.create.as_view(), name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('mypage/', views.mypage, name='mypage'),
    path('<int:id>/delete', views.delete, name='delete'),
]