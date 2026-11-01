from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm


def lista_materiales(request):
    materiales = Material.objects.all()
    return render(
        request,
        'catalogo/materiales.html',
        {'materiales': materiales}
    )


def detalle_material(request, id):
    material = get_object_or_404(Material, id=id)

    return render(
        request,
        'catalogo/detalle_material.html',
        {'material': material}
    )


def crear_material(request):

    if request.method == 'POST':
        form = MaterialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('materiales')

    else:
        form = MaterialForm()

    return render(
        request,
        'catalogo/crear_material.html',
        {'form': form}
    )


def editar_material(request, id):

    material = get_object_or_404(Material, id=id)

    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            instance=material
        )

        if form.is_valid():
            form.save()
            return redirect('materiales')

    else:
        form = MaterialForm(instance=material)

    return render(
        request,
        'catalogo/editar_material.html',
        {
            'form': form,
            'material': material
        }
    )


def eliminar_material(request, id):

    material = get_object_or_404(Material, id=id)

    if request.method == 'POST':
        material.delete()
        return redirect('materiales')

    return render(
        request,
        'catalogo/eliminar_material.html',
        {'material': material}
    )