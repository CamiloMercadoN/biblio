from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    loaned_to = models.CharField(max_length=255, blank=True, null=True)
    loan_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
