

from django.shortcuts import render, redirect
from .models import Medicine

def medicine_list(request):
    if request.method == 'POST':
        Medicine.objects.create(
            
            name=request.POST['name'],
            description=request.POST['description'],
            mrp=request.POST['MRP'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            mfg_date=request.POST['MFG'],
            expiry_date=request.POST['expire']
        )
        return redirect('medicine_list')  # Redirect to avoid duplicate submissions
    
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})


def medicine_home(request):
    return render(request, 'Medicine/medicine_home.html')





# Create your views here.
