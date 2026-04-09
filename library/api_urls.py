from django.urls import path
from .views import (
    HealthView,
    BookListCreateAPIView,
    BookRetrieveAPIView,
    LoanBookAPIView,
    ReturnBookAPIView,
)

urlpatterns = [
    path("", HealthView.as_view(), name="api-health"),
    path("books/", BookListCreateAPIView.as_view(), name="api-book-list-create"),
    path("books/<int:pk>/", BookRetrieveAPIView.as_view(), name="api-book-detail"),
    path("books/<int:pk>/loan/", LoanBookAPIView.as_view(), name="api-book-loan"),
    path("books/<int:pk>/return/", ReturnBookAPIView.as_view(), name="api-book-return"),
]
