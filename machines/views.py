from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def monitor_tb(request):
    return render(request,'Monitor-tb.html')

def CPU_tb(request):
    return render(request,'CPU-tb.html')

def keyboard_tb(request):
    return render(request,'Keyboard-tb.html')

def mouse_tb(request):
    return render(request,'Mouse-tb.html')

def display_monitor(request):
    items = Monitor.objects.all()
    context={
        'items' : items,
        
    }
    return render(request,'monitor-tb.html',context)



def display_mouse(request):
    items = Mouse.objects.all()
    context={
        'items' : items,
        
    }
    return render(request,'mouse-tb.html',context)




def display_CPU(request):
    items = CPU.objects.all()
    context={
        'items' : items,
        
    }
    return render(request,'CPU-tb.html',context)




def display_keyboard(request):
    items = Keyboard.objects.all()
    context={
        'items' : items,
        
    }
    return render(request,'keyboard-tb.html',context)

def add_monitor(request):
    if request.method == "POST":
        form=MonitorForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    else:
        form = MonitorForm()
        return render(request, 'add_new.html',{'form':form})
    
    
def add_cpu(request):
    if request.method == "POST":
        form=CPUForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    else:
        form = CPUForm()
        return render(request, 'add_new.html',{'form':form})
    
    
def add_keyboard(request):
    if request.method == "POST":
        form=KeyboardForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    else:
        form = KeyboardForm()
        return render(request, 'add_new.html',{'form':form})
    
    
def add_mouse(request):
    if request.method == "POST":
        form=MouseForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    else:
        form = MouseForm()
        return render(request, 'add_new.html',{'form':form})
    
def edit_device(request, pk, model, cls):
    item= get_object_or_404(model, pk=pk)
    
    if request.method == "POST":
        form=cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form=cls(instance=item)
        
        return render(request, 'edit_item.html',{'form':form})
    
def edit_monitor(request, pk):
    return edit_device(request, pk, Monitor, MonitorForm)

def edit_cpu(request, pk):
    return edit_device(request, pk, CPU, CPUForm)

def edit_keyboard(request, pk):
    return edit_device(request, pk, Keyboard, KeyboardForm)

def edit_mouse(request, pk):
    return edit_device(request, pk, Mouse, MouseForm)

def delete_monitor(request, pk):
    Monitor.objects.filter(id=pk).delete()
    
    items=Monitor.objects.all()
    
    context = {
        'items':items
    }
    
    return render(request,'Monitor-tb.html',context)

def delete_keyboard(request, pk):
    Keyboard.objects.filter(id=pk).delete()
    
    items=Keyboard.objects.all()
    
    context = {
        'items':items
    }
    
    return render(request,'Keyboard-tb.html',context)

def delete_cpu(request, pk):
    CPU.objects.filter(id=pk).delete()
    
    items=CPU.objects.all()
    
    context = {
        'items':items
    }
    
    return render(request,'CPU-tb.html',context)

def delete_mouse(request, pk):
    Mouse.objects.filter(id=pk).delete()
    
    items=Mouse.objects.all()
    
    context = {
        'items':items
    }
    
    return render(request,'Mouse-tb.html',context)