from django.urls import path
from . import views

app_name='app_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/',views.log_in, name='login' ),
    path('logout/',views.log_out, name='logout' ),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.user_change, name='edit_profile'),
    path('password/', views.change_pass, name='change_pass'),
    path('add_pro_pic/', views.add_pro_pic, name='add_pro_pic'),
    path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic'),
]
