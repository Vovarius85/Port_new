from django_filters import FilterSet, DateFilter, ModelChoiceFilter, CharFilter
from .models import Post, Author
from django import forms

class PostFilter(FilterSet):
    search_title = CharFilter(
        field_name='title',
        label='Название статьи',
        lookup_expr='icontains'
    )
    search_author = ModelChoiceFilter(
        field_name='author',
        label='Автор',
        queryset=Author.objects.all(),
    )
    time_in__gt = DateFilter(field_name='time_in',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte')


