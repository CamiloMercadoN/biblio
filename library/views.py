from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import BookSerializer


class HealthView(APIView):
    def get(self, request):
        return Response({"message": "Biblioteca DRF lista", "books": Book.objects.count()})


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanBookView(APIView):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if not book.available:
            return Response({"detail": "El libro ya está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        user = request.data.get("user")
        if not user:
            return Response({"detail": "Se requiere el campo 'user'."}, status=status.HTTP_400_BAD_REQUEST)

        book.available = False
        book.loaned_to = user
        book.loan_date = timezone.now()
        book.save()
        return Response(BookSerializer(book).data)


class ReturnBookView(APIView):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.available:
            return Response({"detail": "El libro no está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        book.available = True
        book.loaned_to = None
        book.loan_date = None
        book.save()
        return Response(BookSerializer(book).data)
