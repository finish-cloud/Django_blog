from django.urls import path
from . import views
from .views import ContactFormView, ContactResultView
from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap


from blog.views import (
    IndexView,
    PostDetailView,
    CategoryListView,
    CategoryPostView,
    TagListView,
    TagPostView,
    SearchPostView,
    CommentFormView,
    comment_approve,
    comment_remove,
    ReplyFormView,
    reply_approve,
    reply_remove,
)

app_name = 'blog'

sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:category_slug>/',
         CategoryPostView.as_view(), name='category_post'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
    path('comment/<int:pk>/', CommentFormView.as_view(), name='comment_form'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('reply/<int:pk>/', ReplyFormView.as_view(), name='reply_form'),
    path('reply/<int:pk>/approve/', reply_approve, name='reply_approve'),
    path('reply/<int:pk>/remove/', reply_remove, name='reply_remove'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]


urlpatterns += [
    path('<path:url>', views.flatpage),
]
