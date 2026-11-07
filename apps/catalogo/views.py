from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Material
from .forms import MaterialForm


def lista_materiales(request):

    buscar = request.GET.get('buscar')

    materiales = Material.objects.all()

    if buscar:
        materiales = Material.objects.filter(
            Q(nombre__icontains=buscar) |
            Q(descripcion__icontains=buscar) |
            Q(codigo__icontains=buscar)
        )

    paginator = Paginator(materiales, 5)

    page_number = request.GET.get('page')

    materiales = paginator.get_page(page_number)

    return render(
        request,
        'catalogo/materiales.html',
        {
            'materiales': materiales
        }
    )


def detalle_material(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

    return render(
        request,
        'catalogo/detalle_material.html',
        {
            'material': material
        }
    )


@login_required
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
        {
            'form': form
        }
    )


@login_required
def editar_material(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            instance=material
        )

        if form.is_valid():
            form.save()
            return redirect('materiales')

    else:

        form = MaterialForm(
            instance=material
        )

    return render(
        request,
        'catalogo/editar_material.html',
        {
            'form': form,
            'material': material
        }
    )


@login_required
def eliminar_material(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

    if request.method == 'POST':

        material.delete()

        return redirect('materiales')

    return render(
        request,
        'catalogo/eliminar_material.html',
        {
            'material': material
        }
    )


def agregar_sesion(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

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
    