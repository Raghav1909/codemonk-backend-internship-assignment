from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsVerifiedOrReadOnly


class BookViewSet(viewsets.ModelViewSet, mixins.UpdateModelMixin):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsVerifiedOrReadOnly]

    def get_queryset(self):
        queryset = Book.objects.all()

        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__icontains=author)
        
        publication_year = self.request.query_params.get('publication_year', None)
        if publication_year is not None:
            queryset = queryset.filter(publication_year=publication_year)
        
        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            queryset = queryset.filter(genre__icontains=genre)
        
        price = self.request.query_params.get('price', None)
        if price is not None:
            queryset = queryset.filter(price=price)

        no_of_pages = self.request.query_params.get('no_of_pages', None)
        if no_of_pages is not None:
            queryset = queryset.filter(no_of_pages=no_of_pages)
        
        return queryset


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return super().partial_update(request, *args, **kwargs)