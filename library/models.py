from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    pass


    def __str__(self):
        return self.first_name



     
class Book(models.Model):
    category= models.CharField(max_length= 35)
    title = models.CharField(max_length=35)
    about_the_book= models.CharField(max_length=320)
    book_condition = models.CharField(max_length=320)
    refId= models.CharField(max_length= 50, default= '')
    imageUrl= models.CharField(max_length=950)
    price= models.DecimalField(max_digits=5, decimal_places=2, default=0)
    author= models.CharField(max_length=35)
    copies = models.IntegerField( default= 0)
   
    def __str__(self):
        return f"{self.title}" 



class LibraryStaff(models.Model):
    manager= models.CharField(max_length=100)
    librarian= models.CharField(max_length=100)
    Assistant_librarian= models.CharField(max_length=100)
    
    def __str__(self):
        return self.manager



class Student(models.Model):
    referenceId= models.CharField(max_length=100, default= "")
    studentName = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=30)
    parents=models.CharField(max_length=35,blank=True)
    residence= models.CharField(max_length=35, blank=True)
   
    
    def __str__(self):
        return f"{self.studentName}"



class Author(models.Model):
    first_name=models.CharField(max_length= 20)   
    last_name=models.CharField(max_length= 20)
    date_of_birth= models.CharField(max_length=25)
    nationality= models.CharField(max_length= 20)

    def __str__(self):
        """ a string for representing the model object"""
        return self.first_name





    
    

class BookInstance(models.Model):
    """ represents a specific copy of a book (borrowed...)"""
    studentName= models.CharField(max_length= 35, default="")
    student_refId= models.CharField(max_length= 35, default="")
    category= models.CharField(max_length=35, default="")
    title = models.CharField(max_length=35)
    author= models.CharField(max_length=35)
    refId= models.CharField(max_length=35, default="")
    book_condition= models.CharField(max_length=180)
    dateBorrowed=models.DateField(auto_now_add= True)
    return_date= models.CharField(max_length= 35)
    status= models.CharField(max_length= 100, default="") 
   




    def __str__(self):
        """ string for representing the Model object"""
        return f"BookInstance{self.title}  {self.dateBorrowed.strftime('%Y %b %d')}"

    

