from django.shortcuts import render
#from core.forms import *
from core import views


# Create your views here.
def index(request):
    return render(request,'core/index.html')

'''
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        form.save()
        return redirect('/')
    return render(request, 'core/add_product.html'),
'''