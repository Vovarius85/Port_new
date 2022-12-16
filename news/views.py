from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView
from .models import Post
from .filters import PostFilter
from .forms import CreateNewForm
from django.urls import reverse_lazy


class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class SearchPost(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context

class PostCreate(CreateView):
    form_class = CreateNewForm
    model = Post
    template_name = 'new_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            post_path = self.request.META['PATH_INFO']
            if post_path == '/news/create/':
                post.type_of_post = 'Новость'
            elif post_path == '/articles/create/':
                post.type_of_post = 'Статья'

            return super().form_valid(form)

class PostEdit(UpdateView):
    form_class = CreateNewForm
    model = Post
    template_name = 'new_create.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_post')

