def contador_materiales(request):

    cantidad = 0

    if "reserva" in request.session:

        for item in request.session["reserva"].values():

            cantidad += item["cantidad"]

    return {
        "contador_materiales": cantidad
    }