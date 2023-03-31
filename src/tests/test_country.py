import unittest
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from mongoengine import connect
from ormgap.models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        connect('test_gap_analysis', host='mongomock://localhost')
        self.country = Country(
            iso_2='US',
            name='United States of America'
        )

    def test_create_country(self):
        # Crea un nuevo country
        self.country.save()
        self.assertIsNotNone(self.country.id)

        print(self.country)

        # Verifica que el country haya sido creado exitosamente
        country = Country.objects(id=self.country.id).first()
        self.assertEqual(country.iso_2, 'US')
        self.assertEqual(country.name, 'United States of America')
    
    def test_get_country_by_invalid_id(self):
        # Busca un country por un ID que no existe
        found_country = Country.objects(id='609e996db1751152b09f5555').first()
        self.assertIsNone(found_country)

    def test_get_country_by_iso_2(self):
        self.country.save()

        # Busca el country por su ISO 2
        found_country = Country.objects(iso_2=self.country.iso_2).first()
        self.assertIsNotNone(found_country)

        # Verifica que los datos del country encontrado sean los mismos que los creados previamente
        self.assertEqual(found_country.iso_2, 'US')
        self.assertEqual(found_country.name, 'United States of America')

    def test_get_country_by_invalid_iso_2(self):
        # Busca un country por un ISO 2 que no existe
        found_country = Country.objects(iso_2='XX').first()
        self.assertIsNone(found_country)
    
    def test_update_country(self):
        # Actualiza los datos de un país existente

        self.country.save()

        self.country.name = 'USA'
        self.country.save()

        updated_country = Country.objects(id=self.country.id).first()
        self.assertEqual(updated_country.name, 'USA')

    def test_unique_iso_2(self):
        # Verifica que no se puedan crear dos países con el mismo ISO 2
        self.country.save()
        duplicate_country = Country(
            iso_2='US',
            name='USA',
        )

        with self.assertRaises(Exception) as context:       
            duplicate_country.save()

        self.assertTrue('Tried to save duplicate unique keys (E11000 Duplicate Key Error)' in str(context.exception))

    def test_delete_country(self):
        self.country.save()

        self.country.delete()

        country = Country.objects(id=self.country.id).first()
        self.assertIsNone(country)  
    
    def tearDown(self):
        Country.objects.delete()

if __name__ == '__main__':
    unittest.main()