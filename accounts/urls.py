from django.urls import path, include
from accounts import views
app_name="accounts"
urlpatterns = [
    # path('logout', views.logout, name="logout"),  
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    # path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile/', views.index, name='profile'),
    path('signup/', views.signup, name="signup")
]