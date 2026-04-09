from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="books",
    )
    image = models.ImageField(upload_to="book_images/", blank=True, null=True)
    available = models.BooleanField(default=True)
    loaned_to = models.CharField(max_length=255, blank=True, null=True)
    loan_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
