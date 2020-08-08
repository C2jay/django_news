from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('user-profile/', views.UserProfileView.as_view(), name='userProfile'),
    path('author/<int:pk>/', views.AuthorView.as_view(), name='author-detail'),
]