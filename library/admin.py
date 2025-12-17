from django.contrib import admin
import uuid
from .models import User, Book, Author,  LibraryStaff, BookInstance, Student

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(LibraryStaff)
admin.site.register(BookInstance)
admin.site.register(Student)
admin.site.register(Author)

