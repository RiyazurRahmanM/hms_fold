from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Users
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        if Users.objects.filter(email=request.POST['email']).exists():
            user = Users.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                request.session['user_id'] = user.id
                return redirect(reverse('book_view'))
            else:
                context = {
                    'error' : 'Invalid Password',
            }
            return render(request,'login.html',context)            
        else:
            context = {
                'error' : 'Invalid User',
            }
            return render(request,'login.html',context)

    return render(request,'login.html')

def signup_view(request):
    if request.method=='POST':
        users = Users()
        users.name = request.POST['name']
        users.rollno = request.POST['rollno']
        users.mobileno = request.POST['mobileno']
        users.address = request.POST['address']
        users.email = request.POST['email']
        users.password = request.POST['password']
        users.save()
        return redirect(reverse('login_view'))
    return render(request,'signup.html')

def book_view(request):
    userid = request.session['user_id']
    user = Users.objects.get(id=userid)
    if user.is_hosteller == 'No':
        if request.method == 'POST':
            user.is_hosteller = 'Yes'
            user.save()
            return redirect(reverse('dashboard_view'))
        return render(request,'book.html')
    else:
        return redirect(reverse('dashboard_view'))
    
def dashboard_view(request):
    print("Called")
    userid = request.session['user_id']
    user = Users.objects.get(id=userid)
    print(user.name)
    return render(request,'dashboard.html',{'user' : user})

def hosteladmin_view(request):
    return render(request,'hosteladmin.html')

def hosteladminpage_view(request):
    return render(request,'hosteladminpage.html')