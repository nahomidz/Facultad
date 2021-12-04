from django.shortcuts import redirect, render
from .forms import comentario
from .models import registro
# Create your views here.

def index(request):
    return render(request, 'index.html')

def coment(request):
    data = {
        'form': comentario()
    }
    if request.method == 'POST':
        comen = comentario(data=request.POST)
        if comen.is_valid():
            
            comen.save()
            return redirect('lista')
        else:
         
            data['form'] = comen
    
    return render(request, 'form.html',data)

def listado(request):
    comen = registro.objects.all().order_by('id')
    descripcion = {'comentarios' : comen}
    return render(request, 'lista.html',descripcion)


