from django.test import TestCase
from django.urls import reverse

from .models import Pet


class PetManagementTests(TestCase):
    def setUp(self):
        self.pet_data = {
            'name': 'Milo',
            'pet_type': 'Dog',
            'breed': 'Beagle',
            'age': 3,
            'gender': 'Male',
            'color': 'Tricolor',
            'owner_name': 'Alex Owner',
            'owner_contact': '+1 555 0100',
        }

    def test_create_pet_records_details_and_registration_date(self):
        response = self.client.post(reverse('pet_create'), self.pet_data)

        self.assertRedirects(response, reverse('pets'))
        pet = Pet.objects.get(name='Milo')
        self.assertEqual(pet.owner_contact, '+1 555 0100')
        self.assertIsNotNone(pet.date_registered)

    def test_pet_list_shows_saved_record(self):
        pet = Pet.objects.create(**self.pet_data)

        response = self.client.get(reverse('pets'))

        self.assertContains(response, pet.name)
        self.assertContains(response, pet.owner_contact)

    def test_update_pet_changes_existing_record(self):
        pet = Pet.objects.create(**self.pet_data)
        changed_data = {**self.pet_data, 'name': 'Milo II'}

        response = self.client.post(
            reverse('pet_update', args=[pet.pk]),
            changed_data,
        )

        self.assertRedirects(response, reverse('pets'))
        pet.refresh_from_db()
        self.assertEqual(pet.name, 'Milo II')

    def test_delete_requires_post_confirmation(self):
        pet = Pet.objects.create(**self.pet_data)

        response = self.client.get(reverse('pet_delete', args=[pet.pk]))
        self.assertContains(response, 'Delete Record')
        self.assertTrue(Pet.objects.filter(pk=pet.pk).exists())

        response = self.client.post(reverse('pet_delete', args=[pet.pk]))

        self.assertRedirects(response, reverse('pets'))
        self.assertFalse(Pet.objects.filter(pk=pet.pk).exists())
