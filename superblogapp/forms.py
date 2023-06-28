from django import forms



class UserRegistrationForm(forms.Form):
    
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    cnfrm_pwd=forms.CharField(max_length=20)
        

