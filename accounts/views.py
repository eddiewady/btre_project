from django.shortcuts import render,redirect
from django.contrib import messages, auth
from contacts.models import Contact
from django.contrib.auth.models import User


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)

      messages.success(request, 'Your are now Logged in ')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
      return render(request, 'accounts/login.html')
  
def register(request):
  if request.method == 'POST':
    #Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    #check if passwords match
    if password == password2:
      #check username existance
      if User.objects.filter(username=username).exists():
         messages.error(request, 'username already exist')
         return redirect('register')
      else:
        #check email existance
        if User.objects.filter(email=email).exists():
           messages.error(request, 'Email Already Exist')
        else:
          user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
          #login after register
          # auth.login(request, user)
          user.save()
          messages.success(request, 'You are now Registered')
          return redirect('login')
    else:
      messages.error(request,'passwords do not match')
    return redirect('register')
  else:
   return render(request, 'accounts/register.html')
  
  
def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts':user_contacts
  }
  return render(request, 'accounts/dashboard.html',context)

def logout(request):
  if request.method == 'POST':
     auth.logout(request)
     messages.success(request,'Your successful Logout ')
  return redirect('index')
