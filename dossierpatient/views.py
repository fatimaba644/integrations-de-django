from django.shortcuts import render
from .models import Patient
from .models import CentreDeSante



# Create your views here.
def patient_views(request):
    patients = Patient.objects.all()
    return render(request,'patient.html',{'patient': patient})
    

def praticien_views(request):
    praticiens = Praticiens.objects.all()
    return render(request,'praticien.html',{'praticien': praticien})
    

def centre_de_sante_detail(request,centre_id):
    centre = CentreDeSante.objects.get(id=centre_id)
    return render(request,'centre_de_sante_detail.html',{'centre': centre})


def index(request):
    return render(request,'index.html')
        
        
