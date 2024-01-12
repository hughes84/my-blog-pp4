"""
Nutrition Blog - Forms
----------------
Forms for Nutrition Blog

"""
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Profile



class CommentForm(forms.ModelForm):
    """
    Form class for handling comments.

    This form is based on the Comment model and includes a single field,
    'body', for the comment text.

    Attributes:
        model (class): The Django model associated with this form.
        fields (tuple): A tuple specifying the fields to include in the form.
    """

    class Meta:
        """
        Model to provide metadata to the ModelForm.
        """
        model = Comment
        fields = ('body',)


class ContactForm(forms.Form):
    """
    Form class for handling contact form submissions.

    This form includes fields for the user's name, email, and a message.

    Attributes:
        name (CharField): A field for the user's name, with a maximum length of 100 characters.
        email (EmailField): A field for the user's email address.
        message (CharField): A text area field for the user's message.
    """

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for profile image update
    """
    class Meta:
        model = Profile
        fields = ['image', ]

