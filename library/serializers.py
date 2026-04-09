from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "category",
            "available",
            "loaned_to",
            "loan_date",
            "image_url",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
