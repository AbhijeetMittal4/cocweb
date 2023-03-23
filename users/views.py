from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('Username')
            messages.success(request, f"you din't fail to register{ username }")
            return redirect('blizlalo')
    else:
        form = UserCreationForm
        return render(request , 'user/register.html', {'form':form})
    

