from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from news.models import NewsStory
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

#     return HttpResponse('<h1>User Profile</h1>')


class AuthorView(generic.DetailView):
    model = CustomUser 


class UpdateProfileView(generic.UpdateView):
    model = CustomUser
    template_name = 'users/customuser_update.html'
    fields = ['email', 'profileimg', 'bio']

    def get_success_url(self):
        author_id= self.kwargs['pk']
        success_url = reverse_lazy('users:author-detail', kwargs={'pk':
        author_id})
        return success_url


def change_password(request, pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })
