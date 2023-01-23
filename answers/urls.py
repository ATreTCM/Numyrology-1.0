from django.urls import path
from .views import Users_value, Create_users_value, error

app_name = 'answers'

urlpatterns = [
    path('', Users_value.as_view(), name='create_users_value'),
    path('modal', Create_users_value.as_view(), name='modal'),
    path('error', error, name='404'),
]
