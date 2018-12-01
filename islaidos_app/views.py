from django.shortcuts import render, redirect
from .models import Islaidos, Islaidu_tipai
from .forms import IslaidosForm, TiekejaiForm

#BENDRAS PRADINIS

def sarasas(request):
    islaidos = Islaidos.objects.all().order_by('-data')
    islaidu_tipai = Islaidu_tipai.objects.all().order_by('-aktyvus', 'tipas')
    return render(request, 'sarasas.html', {'islaidos': islaidos, 'islaidu_tipai':islaidu_tipai})


#IŠLAIDOS

def sukurti_is(request):
    form = IslaidosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('sarasas')

    return render(request, 'islaidos-form.html', {'form': form})

def pakeisti_is(request, id):
    islaidu_irasas = Islaidos.objects.get(id=id)
    form = IslaidosForm(request.POST or None, instance=islaidu_irasas)

    if form.is_valid():
         form.save()
         return redirect('sarasas')

    return render(request, 'islaidos-form.html', {'form':form, 'islaidu_irasas': islaidu_irasas})

def istrinti_is(request, id):
    islaidu_irasas = Islaidos.objects.get(id=id)

    if request.method == 'POST':
        islaidos.delete()
        return redirect('sarasas')

    return render(request, 'islaidu-istrynimo-patvirtinimas.html', {'islaidu_irasas': islaidu_irasas})


# IŠLAIDŲ TIPAI

def sukurti_tipa(request):
    form = TiekejaiForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('sarasas')

    return render(request, 'tipas-form.html', {'form': form})

def pakeisti_tipa(request, id):
    islaidu_tipas = Islaidu_tipai.objects.get(id=id)
    form = TiekejaiForm(request.POST or None, instance=islaidu_tipas)

    if form.is_valid():
        form.save()
        return redirect('sarasas')

    return render(request, 'tipas-form.html', {'form': form, 'islaidu_tipas': islaidu_tipas})

def istrinti_tipa(request, id):
    islaidu_tipas = Islaidu_tipai.objects.get(id=id)

    if request.method == 'POST':
        islaidu_tipas.delete()
        return redirect('sarasas')

    return render(request, 'tipo-istrynimo-patvirtinimas.html', {'islaidu_tipas': islaidu_tipas})




