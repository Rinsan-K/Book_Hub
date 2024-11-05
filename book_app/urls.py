from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users_update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('users_delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('users_search/', UserSearchView.as_view(), name='user-search'),

    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books_update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books_delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books_search/', BookSearchView.as_view(), name='book-search'),

    path('login/', UserLoginView.as_view(), name='login'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


