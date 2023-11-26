from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value
    
    def validate_author(self, value):
        if value.isalpha() == False:
            raise serializers.ValidationError("Author name must contain only letters")
        return value
    
    def validate_no_of_pages(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of pages cannot be negative")
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value
    
    def validate_publication_year(self, value):
        currentYear = datetime.now().year

        try:
            int(var)

        except ValueError:
            raise serializers.ValidationError("Publication year must be an integer")

        if value > currentYear:
            raise serializers.ValidationError("Publication year cannot be in the future")
        
        return value
