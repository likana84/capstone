from django.shortcuts import  render  
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse,HttpResponseRedirect 
from django.urls import reverse
from .models import  User,  Book, Author,  Student,  BookInstance, LibraryStaff

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("library:login"))
    else:    
        return render(request, "library/index.html")


def form(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("library:login"))
    else:
       
        return render(request, "library/forms.html")

       

def books(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("library:login"))
    else:
        allBooks= Book.objects.all()
        return render(request, "library/books.html", {"allBooks":allBooks})

def add_books(request):
        # obtain data from the form
    if request.method == "POST":
        category= request.POST.get("addCat")
        title= request.POST.get("addTit")
        about_the_book= request.POST.get("book_theme")
        book_condition= request.POST.get("status")
        refId= request.POST.get("addRef")
        imageUrl= request.POST.get("addUrl")
        price= request.POST.get("addPrice")
        author= request.POST.get("addAut")
        copies= request.POST.get("addCopies")
        print(category,title,about_the_book,book_condition,refId,imageUrl,price,author,copies)

        addBooks= Book()
        addBooks.category= category
        addBooks.title= title
        addBooks.about_the_book= about_the_book
        addBooks.book_condition= book_condition
        addBooks.refId= refId
        addBooks.imageUrl= imageUrl
        addBooks.price= price
        addBooks.author= author
        addBooks.copies= copies
        addBooks.save()
        
        #add book
        return HttpResponse("book added successfully")





     
     
















def book_details(request, id):
        
        book_detail= Book.objects.get(id=id)
        return render(request, "library/book_details.html",{
             'book_detail':book_detail,
             })





def book_borrowed_view(request):
        borrowed_books= BookInstance.objects.all()
        return render(request, "library/book_borrowed.html",{'borrowed_books':borrowed_books})

def book_borrowed(request):
    if request.method == "POST":
        studentName= request.POST.get("student_name_1")
        student_refId= request.POST.get("student_id")
        category=request.POST.get("borCat")
        title= request.POST.get("borTit")
        author= request.POST.get("borAut")
        refId= request.POST.get("borRef")
        book_condition= request.POST.get("borCondition")
        dateBorrowed= request.POST.get("borDat")
        return_date= request.POST.get("retDat")
        status= request.POST.get("borStatus")

        borrowed_book= BookInstance()
        borrowed_book.studentName= studentName
        borrowed_book.student_refId= student_refId
        borrowed_book.category= category
        borrowed_book.title = title
        borrowed_book.author= author
        borrowed_book.refId= refId
        borrowed_book.book_condition= book_condition
        borrowed_book.dateBorrowed= dateBorrowed
        borrowed_book.return_date= return_date
        borrowed_book.status= status
        borrowed_book.save()

        #redirect to index page
        return HttpResponse("successfully borrowed")
    











    

def all_books(request):
    allBooks= Book.objects.all()
    return render(request, "library/all_books.html", {"allBooks":allBooks})




def author(request):
        authors= Author.objects.all()
        return render(request, "library/author.html", {"authors":authors})


def author_profile(request):
        author_profiles=Author.objects.all()
        return render(request, "library/author_profile.html", {"author_profiles":author_profiles})






def student(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("library:login"))
    else:
      
        studentNames= Student.objects.all()
        context= {
            'studentNames':studentNames
        }
        return render(request, "library/student.html", context) 


def add_student(request):
    if request.method == "POST":
        referenceId=request.POST.get('student_1')
        studentName=request.POST.get('student_2')
        phone_number=request.POST.get('student_3')
        parents=request.POST.get('student_4')
        residence=request.POST.get('student_5')
        
        studentProfile= Student()
        studentProfile.referenceId=referenceId
        studentProfile.studentName= studentName
        studentProfile.phone_number= phone_number
        studentProfile.parents= parents
        studentProfile.residence= residence

        studentProfile.save()
        return HttpResponse("REGISTERED")







         
          


     
          
     



  

  






def lib_staff(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("library:login"))
    else:
        library_staff= LibraryStaff.objects.all()
        return render(request, "library/lib_staff.html", {"library_staff":library_staff})  
    



 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username= username, password= password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("library:index"))
        else:
            return render(request, "library/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "library/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("library:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure StudentId matches confirmation
        password = request.POST.get("password")
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "library/register.html", {
                "message": "password must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username,email, password)
            user.save()
        except IntegrityError:
            return render(request, "library/register.html", {
                "message": "username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("library:index"))
    else:
        return render(request, "library/register.html")
