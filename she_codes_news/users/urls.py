from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', views.AuthorView.as_view(), name='author-detail'),
    path('<int:pk>/edit/', views.UpdateProfileView.as_view(), name='update-profile'),
    path('<int:pk>/change-password/', views.change_password, name='change-password'),
]