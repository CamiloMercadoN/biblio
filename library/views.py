from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import BookForm, CategoryForm
from .models import Book, Category
from .serializers import BookSerializer


class HomeView(TemplateView):
    template_name = "library/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_count"] = Book.objects.count()
        context["category_count"] = Category.objects.count()
        context["books"] = Book.objects.all().order_by("title")[:12]
        context["categories"] = Category.objects.all()
        return context


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    login_url = "login"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("book-list-html")
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Agregar libro"
        return context


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"
    login_url = "login"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")

        if action == "loan":
            user = request.POST.get("user")
            if user:
                self.object.available = False
                self.object.loaned_to = user
                self.object.loan_date = timezone.now()
                self.object.save()
        elif action == "return":
            self.object.available = True
            self.object.loaned_to = None
            self.object.loan_date = None
            self.object.save()

        return redirect("book-detail-html", pk=self.object.pk)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("book-list-html")
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar libro"
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("book-list-html")
    login_url = "login"


def cerrar_sesion(request):
    logout(request)
    return redirect("login")


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "library/category_list.html"
    context_object_name = "categories"
    login_url = "login"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "library/category_form.html"
    success_url = reverse_lazy("category-list-html")
    login_url = "login"


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "library/category_form.html"
    success_url = reverse_lazy("category-list-html")
    login_url = "login"


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "library/category_confirm_delete.html"
    success_url = reverse_lazy("category-list-html")
    login_url = "login"


class HealthView(APIView):
    def get(self, request):
        return Response({"message": "Biblioteca DRF lista", "books": Book.objects.count()})


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanBookAPIView(APIView):
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


class ReturnBookAPIView(APIView):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.available:
            return Response({"detail": "El libro no está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        book.available = True
        book.loaned_to = None
        book.loan_date = None
        book.save()
        return Response(BookSerializer(book).data)
