def agregar_sesion(request, id):

    material = get_object_or_404(Material, id=id)

    materiales = request.session.get(
        'materiales_sesion',
        []
    )

    materiales.append(material.nombre)

    request.session['materiales_sesion'] = materiales

    return redirect('materiales')


def lista_sesion(request):

    materiales = request.session.get(
        'materiales_sesion',
        []
    )

    return render(
        request,
        'catalogo/lista_sesion.html',
        {
            'materiales': materiales
        }
    )


def vaciar_sesion(request):

    request.session['materiales_sesion'] = []

    return redirect('lista_sesion')