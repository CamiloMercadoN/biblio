from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="library/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("books/", BookListView.as_view(), name="book-list-html"),
    path("books/add/", BookCreateView.as_view(), name="book-add-html"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail-html"),
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book-edit-html"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete-html"),
    path("categories/", CategoryListView.as_view(), name="category-list-html"),
    path("categories/add/", CategoryCreateView.as_view(), name="category-add-html"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category-edit-html"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete-html"),
]
