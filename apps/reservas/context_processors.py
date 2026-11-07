def contador_materiales(request):

    cantidad = 0

    if "reserva" in request.session:

        cantidad = len(
            request.session["reserva"]
        )

    return {
        "contador_materiales": cantidad
    }

