from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True, null=False,blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_pages = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.author}"