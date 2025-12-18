from django.contrib import admin
from django.urls import path 
from .import views 

app_name= 'library'

urlpatterns = [
   path("", views.index, name="index"),
   path("student", views.student, name="student"),
   path("books", views.books, name= "books"),
  
   path("add_books", views.add_books, name= "add_books"),
   path("add_student", views.add_student, name="add_student"),
   path("lib_staff", views.lib_staff, name="lib_staff"),
   path("book_borrowed_view", views.book_borrowed_view, name="book_borrowed_view"),
   path("book_borrowed", views.book_borrowed, name="book_borrowed"),
   path("book_details/<int:id>/", views.book_details, name= "book_details_name"),
   path("all_books", views.all_books, name= "all_books"),
   path("author", views.author, name= "author"),
   path("author_profile", views.author_profile, name= "author_profile"),
   path("form", views.form, name= "form"),
   path("login", views.login_view, name="login"),
   path("register", views.register, name="register"),
   path("logout", views.logout_view, name="logout"),



]