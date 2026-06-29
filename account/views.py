from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from account.forms import MyUserCreationForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'issues:project_list')
        else:
            context['has_error'] = True
    return render(request, 'account/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('account:login')

def register_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'issues:project_list')
    else:
        form = MyUserCreationForm()
    return render(request, 'account/register.html', context={'form': form})



