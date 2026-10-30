from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def iniciar_sesion(request):
    
    if request.method == "POST":
        usuario = authenticate(request,
            username = request.POST["username"],
            password = request.POSR["password"]
        )

    if usuario is not None:
        login(request, usuario)
        redireccion = request.GET.get("next", "/asistencia/")
        return redirect(redireccion)

        return render(request,
        "usuarios/login.html",
        {"Usuario o contraseña incorrectas"}
        )

    return render(request,
    "usuarios/login.html",
    )

def cerrar_sesion(request):

    logout(request)

    return redirect("/usuarios/login/")