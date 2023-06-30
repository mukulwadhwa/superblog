from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def my_view(request):
    context = {
        'message': 'Hello, World!'
    }
    return render(request, 'login.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            # Perform additional authentication checks if necessary
            # For example, you could use Django's built-in authentication system or third-party libraries
            return redirect('home')  # Redirect to the home page after successful login
        
        except User.DoesNotExist:
            error = 'Invalid username or password'
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
