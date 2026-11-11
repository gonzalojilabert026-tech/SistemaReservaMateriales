from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Material, Categoria
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

    paginator = Paginator(
        materiales,
        8
    )

    page_number = request.GET.get('page')

    materiales = paginator.get_page(
        page_number
    )

    return render(
        request,
        'catalogo/materiales.html',
        {
            'materiales': materiales
        }
    )


@login_required
def lista_sesion(request):

    ids = request.session.get(
        'materiales_sesion',
        []
    )

    materiales = Material.objects.filter(
        id__in=ids
    )

    if not materiales.exists():

        return render(
            request,
            'reservas/carrito.html'
        )

    return render(
        request,
        'catalogo/lista_sesion.html',
        {
            'materiales': materiales
        }
    )

def detalle_material(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

    relacionados = Material.objects.filter(
        categoria=material.categoria
    ).exclude(
        id=material.id
    )[:4]

    return render(

        request,

        'catalogo/detalle_material.html',

        {
            'material': material,
            'relacionados': relacionados
        }

    )

@login_required
@staff_member_required
def crear_material(request):

    if request.method == 'POST':

        nueva_categoria = request.POST.get(
            'nueva_categoria'
        )

        if nueva_categoria:

            categoria, creada = Categoria.objects.get_or_create(
                nombre_categoria=nueva_categoria
            )

            datos = request.POST.copy()
            datos['categoria'] = categoria.id

            form = MaterialForm(
                datos,
                request.FILES
            )

        else:

            form = MaterialForm(
                request.POST,
                request.FILES
            )

        if form.is_valid():

            form.save()

            return redirect(
                'catalogo:materiales'
            )

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
@staff_member_required
def editar_material(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

    if request.method == 'POST':
        form = MaterialForm(
            request.POST,
            request.FILES,
            instance=material
        )

        if form.is_valid():
            form.save()
            return redirect('catalogo:materiales')

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
@staff_member_required
def eliminar_material(request, id):

    material = get_object_or_404(
        Material,
        id=id
    )

    if request.method == 'POST':

        material.delete()

        return redirect('catalogo:materiales')

    return render(
        request,
        'catalogo/eliminar_material.html',
        {
            'material': material
        }
    )


@login_required
def agregar_sesion(request, id):

    materiales = request.session.get(
        'materiales_sesion',
        []
    )

    if id not in materiales:
        materiales.append(id)

    request.session['materiales_sesion'] = materiales
    request.session.modified = True

    return redirect(
        'catalogo:lista_sesion'
    )

@login_required
def comprobante(request):

    return render(
        request,
        'catalogo/comprobante.html'
    )


def vaciar_sesion(request):

    request.session['materiales_sesion'] = []

    return redirect('catalogo:lista_sesion')
    