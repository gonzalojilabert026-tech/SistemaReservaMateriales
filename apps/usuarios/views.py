from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout


def iniciar_sesion(request):

    if request.user.is_authenticated:
        return redirect("perfil")

    form = AuthenticationForm()

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            usuario = form.get_user()

            login(
                request,
                usuario
            )

            return redirect("perfil")

    return render(
        request,
        "usuarios/login.html",
        {
            "form": form
        }
    )


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def perfil(request):
    return render(
        request,
        'usuarios/perfil.html'
    )
    
def registro_view(request):

    return render(
        request,
        'usuarios/registro.html'
    )