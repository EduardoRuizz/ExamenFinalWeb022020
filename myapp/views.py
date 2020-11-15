from django.shortcuts import render, redirect

from myapp.models import Producto 


from myapp.forms import ProductoForm

# Create your views here.


def addnew(request):  
    if request.method == "POST":  
        form = ProductoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = ProductoForm()  
    return render(request,'index.html',{'form':form})  
    

def index(request):  
    productos = Producto.objects.all()  
    return render(request,"show.html",{'productos':productos})  

def edit(request, id):  
    productos= Producto.objects.get(id=id)  
    return render(request,'edit.html', {'productos':productos}) 


def update(request, id):  
    productos = Producto.objects.get(id=id)  
    form = ProductoForm(request.POST, instance = productos)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'productos': productos})  

def destroy(request, id):  
    productos = Producto.objects.get(id=id)  
    productos.delete()  
    return redirect("/")  