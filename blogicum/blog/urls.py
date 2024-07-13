from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'

# Posts
posts = [
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path(
        '<int:post_id>/edit_comment/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment',
    ),
    path(
        '<int:post_id>/delete_comment/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment',
    ),
]

# Profile
profile = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.profile, name='profile'),
]

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # Category
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
    path('posts/', include(posts)),
    path('profile/', include(profile)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
