from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user:
                login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})
