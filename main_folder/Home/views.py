import imp
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
#this form conains username and password that is used for login form
from django.contrib.auth import login,authenticate #here we use UserRegistration form instead of usercreaton form
#login is used to login to website.and authenticate is used for validating certain
#credintial such as username,password
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.http import HttpResponse 
from .models import book
from .forms import BookCreate
from django.contrib.auth.models import User
#this inherits usercreation form
# Create your views here.
def home(request):
  return render(request,'Home/base.html')
def register(request):

   if request.method =='POST':
     form=UserRegisterForm(request.POST)
     if form.is_valid():
        
        form.save()
        username=form.cleaned_data['username']
        
        messages.success(request,f'Your{username} account has been created! you are now able to login')
        return redirect('login')
   else:
       form=UserRegisterForm()
     
   return render(request,'Home/register.html',  {'form':form})
def login_form(request):
  
  if request.method=="POST":
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():

      username=form.cleaned_data['username']
      
      password=form.cleaned_data['password']
      user=authenticate(username=username,password=password)
      if user is not None:
        login(request,user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('main_home')
      else:
        messages.error(request,"Invalid username or password.")
    else:
      messages.error(request,"Invalid username or password.")
  form=AuthenticationForm()
  return render(request,'Home/login.html',context={"login_form":form})
def logout_view(request):
    logout(request)
    messages.info(request, f"You are now logged out")
    return render(request,'Home/logout.html')

def index(request):
  shelf=book.objects.all()
  
  return render(request,'Home/library.html',{'shelf':shelf})
def upload(request):
  upload=BookCreate()
  if request=='POST':
    upload=BookCreate(request.POST,request.FILES)#data is sent to boolcreate table and files are for images and 
    #for other files
    if upload.is_valid():
      upload.save()
      return redirect('library')
    else :
      
      return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
  else:
        return render(request, 'Home/upload_form.html', {'upload_form':upload})
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = book.objects.get(id = book_id)
    except book.DoesNotExist:
        return redirect('library')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('library')
    return render(request, 'Home/upload_form.html', {'upload_form':book_form})

# def check_admin1(request):
#     if request.method=="POST":
#       form=AuthenticationForm(request,data=request.POST)
#       if request.user.is_superuser:
#         users=form.objects.all() 
#         return render(request,'Home/admin_panel.html',{'users':users})
#       else:
#         return render(request,'Home/base.html')
#     else:
#        form=AuthenticationForm()
#        return render(request,'Home/admin.html',{'login_form':form})
        


def check_admin1(request):
  
  if request.method=="POST":
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():

      
      user=authenticate(username='username',password='password')
      if request.user.is_superuser==True:
        
        login(request,user)
        
        return redirect("admin_panel")
      else:
        messages.error(request,"Invalid username or password.")
    else:
      messages.error(request,"Invalid username or password.")
  form=AuthenticationForm()
  return render(request,"Home/admin.html",context={'login_form':form})


# def panel(request):

#    if request.method =='POST':
#      form=UserRegisterForm(request.POST)
#      if form.is_valid():
        
#         form.save()
        
       
#         return redirect('admin_panel')
#    else:
#        form=UserRegisterForm()
     
#    return render(request,'Home/create.html',  {'form':form})
def show(request):
  
   if request.method =='POST':
     
     form=UserRegisterForm(request.POST)
     if form.is_valid():
        form=UserRegisterForm(request.POST)
        # nm=form.cleaned_data['username']
        # em=form.cleaned_data['email']
        # ps=form.cleaned_data['password']
        # reg=User(username=nm,email=em,password=ps)

        form.save()
        form=UserRegisterForm()

     else:
       form=UserRegisterForm()
   form=UserRegisterForm()
   disp=User.objects.all() 
   return render(request,'Home/admin_panel.html',  {'form':form,'user':disp})
def update(request,pk):
    user_id = int(pk)
    try:
        reg = User.objects.get(id = user_id)
    except reg.DoesNotExist:
        return redirect('admin_panel')
    reg_create= UserRegisterForm(request.POST or None,instance=reg)
    if reg_create.is_valid():
       reg_create.save()
       return redirect('admin_panel')
    return render(request, 'Home/upload_form.html', {'upload_form':reg_create})
def delete_user(request,pk):
    userid=User.objects.get(id=pk)
    userid.delete()
    return redirect("admin_panel")       

    