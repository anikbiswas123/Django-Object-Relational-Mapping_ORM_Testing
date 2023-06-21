from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name  

class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    pubdate = models.DateField()

    def __str__(self):
        return self.name
    
    @property
    def get_authors(self):
        # return ", ".join([author.name for author in self.authors.all()])
        return ", ".join([str(author) for author in self.authors.all()]) # দুইটির যে কোন একটি use করা যায়।
    
    @property
    def get_publisher(self):
        return self.publisher.name
    

    
class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
    @property
    def get_books(self):
        return ", ".join([book.name for book in self.books.all()])
    
    #-------------------------------------------------------------
    # @property
    # def get_authors(self):
    #     return ", ".join([author.name for book in self.books.all() for author in book.authors.all()])


    # @property
    # def get_authors(self):  # উপরের টি এবং এটি এবং নিচের টি , যে কোন টি use করা যাবে।
    #     authors = []
    #     for book in self.books.all():
    #         authors.extend(book.authors.all())
    #     return ", ".join([author.name for author in authors])


    # @property
    # def get_authors(self):
    #     authors = []
    #     for book in self.books.all():
    #         authors.extend([str(author) for author in book.authors.all()])
    #     return ", ".join(authors)


    @property
    def get_authors(self):
        authors = []
        for book in self.books.all():
            for author in book.authors.all():
                authors.extend([str(author)])
        return ", ".join(authors)

    #______________________________________________________________

    #-------------------------------------------------------------
    # @property
    # def get_publisher(self):
    #     return ", ".join([book.publisher.name for book in self.books.all()])
    
    
    @property
    def get_publisher(self):  # উপরের টি এবং এটি একই, যে কোন টি use করা যাবে।
        publishers = []
        for book in self.books.all():
            publishers.append(book.publisher.name)
        return ", ".join(publishers)

    #______________________________________________________________

    """NOTE এই দুইটি method Querry set return করে, 

    @property
    def get_authors(self):
        authors = set()
        for book in self.books.all():
            authors.update(book.authors.all())
        return authors
    
    @property

    def get_publisher(self):
        publishers = set()
        for book in self.books.all():
            publishers.add(book.publisher)
        return publishers

    """
