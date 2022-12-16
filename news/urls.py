from django.urls import path
from .views import PostsList, PostDetail, SearchPost, PostCreate, PostEdit, PostDelete


urlpatterns = [
   path('', PostsList.as_view(), name = 'all_post'),
   path('<int:pk>', PostDetail.as_view(), name = 'new'),
   path('search', SearchPost.as_view()),
   path('create/', PostCreate.as_view(), name = 'article_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='article_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
]
