from django import forms
from django.core.exceptions import ValidationError

from .models import Post

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


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

class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
