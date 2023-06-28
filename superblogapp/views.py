from django.shortcuts import render, redirect
from superblogapp.forms import UserRegistrationForm
from .models import Sigin

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cnfrm_pwd=form.cleaned_data['cnfrm_pwd']

            # Create a new user object
            user = Sigin(email=email, password=password,cnfrm_pwd=cnfrm_pwd)
            user.save()
            return redirect("signup_success")  # Replace 'signup_success' with your success URL name
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})
   


