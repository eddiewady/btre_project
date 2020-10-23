from django.shortcuts import render,redirect

def login(request):
  if request.method == 'POST':
    print("SUCCESSFULLY lOGIN IN")
    return redirect('index')
  return render(request, 'accounts/login.html')
  
def register(request):
  if request.method == 'POST':
     print("pOST sUBMITTED")
     return redirect('login')
  else:
   return render(request, 'accounts/register.html')
  
def dashboard(request):
  return render(request, 'accounts/dashboard.html')

def logout(request):
  return redirect('index')
