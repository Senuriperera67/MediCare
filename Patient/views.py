from django.shortcuts import render



from .models import Patient

def patient_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')
        nic = request.POST.get('nic')
        problem = request.POST.get('problem')

        # Validation for age
        if age < 18:
            return render(request, 'your_template.html', {'error': 'Age must be 18 or above'})

        # Save the patient data
        Patient.objects.create(name=name, age=age, sex=sex, nic=nic, problem=problem)

    # Fetch all patients from the database
    patients = Patient.objects.all()

    return render(request, 'your_template.html', {'patients': patients})


def patient_home(request):
    return render(request, 'Patient/patient_home.html')  



# Create your views here.
