from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')       # form.cleaned data returns a dictionary of validated form inputs
            messages.success(request, f'Your account has been created, You can now login!')
            return redirect('login')
    else:                                                      
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})
    
@login_required             # After logging in this will redirect to the profile page only, and not to the home page
def profile(request):       # This feature is very helpful in all web apps. This is specified by the next parameter in the url
    return render(request, 'users/profile.html')
    
