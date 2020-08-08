from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from news.models import NewsStory
# Create your views here.

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

#     return HttpResponse('<h1>User Profile</h1>')


class AuthorView(generic.DetailView):
    model = CustomUser    