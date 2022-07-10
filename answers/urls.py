from django.urls import path
from . import views

app_name = 'answers'

urlpatterns = [
    path('comment/', views.Comments_detail.as_view(), name='comment'),
    path('comments/', views.Comments_list.as_view(), name='comments'),
    path('service/', views.Service_detail.as_view(), name='service'),
    path('services/', views.Services_list.as_view(), name='services'),
    path('', views.create_users_value, name='create_users_value'),
]
