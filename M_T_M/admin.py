from django.contrib import admin
from  .models import Book, Author, Publisher, Store
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Publisher)
# admin.site.register(Store)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pages', 'price', 'rating', 'pubdate', 'get_authors', 'get_publisher']

    """
        In the get_authors method, you need to iterate over the related authors using obj.authors.all() since it's a ManyToMany 
        field. Then you can retrieve the name of each author and join them using ", " to display a comma-separated list of authors.
    """
    """NOTE যেহেতু এই দুইটি Method কে Book Model এর সাথে Declare করা হয়েছে তাই এখানে আর লিখার দরকার হয়নি, আমরা এগুলোকে direct access করতে পারছি এখান থেকে।

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    
    def get_publisher(self, obj):
        return obj.publisher.name
    
    get_authors.short_description = 'Auther'
    get_publisher.short_description = 'Publisher'

    """

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    list_display = ['id', 'name', 'get_books', 'get_publisher', 'get_authors']

    # def display_books(self, obj):
    #     return ", ".join([book.name for book in obj.books.all()])

    # display_books.short_description = 'Books'