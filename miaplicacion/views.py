from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, BusquedaForm, ClienteForm
from .models import Categoria, Producto

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o realizar acciones adicionales después de guardar el formulario
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o realizar acciones adicionales después de guardar el formulario
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def buscar_productos(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            # Hacer algo con los resultados, como pasarlos al template para mostrarlos
    else:
        form = BusquedaForm()
    return render(request, 'buscar_productos.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_agregado')  # Redirigir a la página de confirmación de cliente agregado
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def cliente_agregado(request):
    return render(request, 'cliente_agregado.html')
