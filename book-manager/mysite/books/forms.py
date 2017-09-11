from django import forms
from django.contrib.auth.models import User
from .models import Review


class BookSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search by Title or Author!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'text')
