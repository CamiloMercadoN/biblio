from django.urls import path
from .views import (
    HealthView,
    BookListCreateView,
    BookRetrieveView,
    LoanBookView,
    ReturnBookView,
)

urlpatterns = [
    path("", HealthView.as_view(), name="health"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookRetrieveView.as_view(), name="book-detail"),
    path("books/<int:pk>/loan/", LoanBookView.as_view(), name="book-loan"),
    path("books/<int:pk>/return/", ReturnBookView.as_view(), name="book-return"),
]
