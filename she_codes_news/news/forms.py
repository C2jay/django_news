from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory, Comment

class StoryForm(ModelForm):
    pub_date = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label='Publication Date'
    )

    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content']
        labels = {'image':'Image URL'}

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form',
                    'placeholder': 'Article Title',
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
                attrs={
                    'class': 'form',
                    'placeholder': 'Enter image URL here'
                }
            ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')