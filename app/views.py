from django.shortcuts import render, redirect
from app.forms import ClienteForm
from app.models import Cliente

# Create your views here.
def home(request):
    data = {}
    data['db'] = Cliente.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ClienteForm
    return render(request, 'form.html', data)

def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)




