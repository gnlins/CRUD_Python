from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros

# Create your views here.
def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return render(request,'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)
