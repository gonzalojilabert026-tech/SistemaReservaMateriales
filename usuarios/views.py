from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')

    else:
        form = UserCreationForm()

    return render(
        request,
        'usuarios/registro.html',
        {'form': form}
    )


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'usuarios/login.html',
        {'form': form}
    )


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def perfil(request):
    return render(
        request,
        'usuarios/perfil.html'
    )