from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form',
                    'placeholder': 'Article Title',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form',
                    'placeholder': 'Author Name'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form',
                    'id': 'box-size',
                    'placeholder': 'Article Content'
                }
            ),
            'image':forms.URLInput(
            ),
        }


