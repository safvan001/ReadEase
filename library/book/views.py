from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from book.models import book,student
from book.forms import bookform
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pdf=request.FILES['u']
        cover=request.FILES['f']

        b=book.objects.create(title=t,author=a,price=p,pdf=pdf,cover=cover)
        b.save()
        return home(request)
    return render(request,'add.html')
def addstudent(request):
    if (request.method == "POST"):
        f = request.POST['f']
        l = request.POST['l']
        v = request.POST['v']
        s = request.POST['s']

        b = student.objects.create(f_name=f,l_name=l,age=v,place=s)
        b.save()
        return home(request)
    return render(request,'addstudent.html')
def add1(request):
    f=bookform() #create empty form object
    if (request.method=="POST"):
        print(request.POST) #used to print entered values in terminal
        f=bookform(request.POST,request.FILES) #create form object using values received from form
                                 #request.POST-dictionary sent from template

        if(f.is_valid()):
            f.save()
        return home(request)
    return render(request,'add1.html',{'form':f})
def factorial(request):
    if (request.method == "POST"):
        n = int(request.POST['n'])
        f=1
        for i in range(1,n+1):
            f=f*i
        return render(request,'factorial.html',{'fact':f})
    return render(request, 'factorial.html')
def calculator(request):
    if request.method == "POST":
        n1 = int(request.POST['n1'])
        n2 = int(request.POST['n2'])
        s = n1 + n2
        p = n1 * n2
        q = n1 / n2
        d = n1 - n2
        return render(request, 'calculationResult.html', {'sum': s, 'product': p, 'quotient': q, 'difference': d})
    return render(request, 'calculator.html')

def veiwbook(request):
    b=book.objects.all()
    return render(request,'veiwbook.html',{'book':b})
def veiw_book(request,p):
    b=book.objects.get(id=p)
    return render(request,'veiwbook2.html',{'book':b})
def veiw(request):
    s=student.objects.all()
    return render(request,'veiwstudent.html',{'student':s})
def delete_book(request,p):
    b=book.objects.get(id=p)
    b.delete()
    return veiwbook(request)
def update_book(request,p):
    b=book.objects.get(id=p)
    form=bookform(instance=b)
    if(request.method == "POST"):
        print(request.POST)  # used to print entered values in terminal
        f = bookform(request.POST, request.FILES, instance=b)
        if (f.is_valid()):
            f.save()
            return veiwbook(request)
    return render(request,'add1.html',{'form':form})
def search(request):
    if (request.method == "POST"):
        s=request.POST['srh']
        if s:
            match=book.objects.filter(Q(title__icontains=s)|Q(author__icontains=s))
            if match:
                return render(request,'search.html',{'m':match})
            else:
                messages.error(request,"no result found")

    return render(request,'search.html')
def register(request):
    if(request.method == "POST"):
        u=request.POST['u']
        fs=request.POST['fs']
        ls = request.POST['ls']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if p==cp:
            user=User.objects.create_user(username=u,first_name=fs,last_name=ls,email=e,password=p)
            user.save()
            return home(request)
        else :
            messages.error(request, 'Passwords do not match')
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
      u=request.POST['u']
      p=request.POST['p']
      user = authenticate(username=u,password=p)
      if user:
        login(request,user)
        return home(request)
      else:
         messages.error(request,'password is invalid')

    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return home(request)

# Create your views here.
