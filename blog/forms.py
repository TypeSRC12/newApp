from django import forms
from .models import Comment, Contact

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['blog']

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"