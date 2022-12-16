from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class CreateNewForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'post_category']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Заголовок должен отличаться от содержания"
            )

        return cleaned_data
