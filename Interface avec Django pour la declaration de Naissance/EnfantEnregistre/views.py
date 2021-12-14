from django.shortcuts import render
from .models import infoEnfant,infoSurPersonnel
# Create your views here.
def listeEnfantEnregistrer(request):
    listeEnfant=infoEnfant.objects.all()
    enfant={'listeEnfants':listeEnfant}
    return render(request,'listeEnfantEnregistrer/listeEnfantEnregistrer.html',enfant)

def info_Personnel(request):
    listePersonnel=infoSurPersonnel.objects.all()
    personnel={'listePersonnels':listePersonnel}
    return render(request,'inforSurPersonnel/inforSurPersonnel.html',personnel)

def detail(request,id):
    detail=infoEnfant.objects.get(id=id)
    detaills={'details':detail}
    return render(request,'detail/detail.html',detaills)