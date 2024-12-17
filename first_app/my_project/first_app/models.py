from django.db import models


# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=50, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"


class Publisher(models.Model):
    name = models.TextField(max_length=250)
    address = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name} - {self.address}"


class Author(models.Model):
    name = models.TextField(max_length=250)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.birth_date}"


class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField(null=True)
    biography = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.author.name} - {self.author} - {self.website} - {self.biography}"


class Book(models.Model):
    title = models.TextField(max_length=250)
    pub_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return f"{self.title} - {self.pub_date} - {self.publisher.name}"