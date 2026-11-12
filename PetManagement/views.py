from django.shortcuts import get_object_or_404, redirect, render

from .forms import PetForm
from .models import Pet


def index(request):
    return render(request, 'PetCare/index.html')


def pet_list(request):
    pets = Pet.objects.order_by('-date_registered', '-id')
    return render(request, 'PetCare/pet_list.html', {'pets': pets})


def pet_create(request):
    form = PetForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pets')
    return render(request, 'PetCare/pet_form.html', {'form': form, 'title': 'Add a pet'})


def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    form = PetForm(request.POST or None, instance=pet)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pets')
    return render(request, 'PetCare/pet_form.html', {
        'form': form,
        'title': 'Edit pet',
        'pet': pet,
    })


def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets')
    return render(request, 'PetCare/pet_confirm_delete.html', {'pet': pet})


def services(request):
    return render(request, 'PetCare/services.html')


def tips(request):
    return render(request, 'PetCare/tips.html')


def contact(request):
    return render(request, 'PetCare/contact.html')