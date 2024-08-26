from django.urls import path
from .views import fetch_data, store_data,register,my_login,user_logout


urlpatterns = [
    path('', fetch_data, name='fetch-data'),
    path('store-data/',store_data, name='store-data'),
    path('register/', register, name='register' ),
    path('login/', my_login, name='login'),
    path('logout',user_logout, name='logout'),
]
