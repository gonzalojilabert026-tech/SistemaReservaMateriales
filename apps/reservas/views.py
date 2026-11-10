from django.shortcuts import render

def carrito(request):

    materiales = request.session.get(
        'materiales_sesion',
        []
    )

    if not materiales:
        return render(
            request,
            'catalogo/carrito_vacio.html'
        )

    return render(
        request,
        'catalogo/carrito.html',
        {
            'materiales': materiales
        }
    )