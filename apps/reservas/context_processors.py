def contador_materiales(request):

    materiales = request.session.get(
        "materiales_sesion",
        []
    )

    return {
        "contador_materiales": len(materiales)
    }
