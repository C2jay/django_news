from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('author/<int:pk>/', views.AuthorView.as_view(), name='author-detail'),
]