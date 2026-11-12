from django.shortcuts import render

from PetManagement.models import Pet


def pet_list(request):
    pets = Pet.objects.order_by('-date_registered', '-id')
    return render(request, 'PetCare/pet_list.html', {'pets': pets})
