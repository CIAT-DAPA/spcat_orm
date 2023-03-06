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
    
    
    def tearDown(self):
        Country.objects.delete()

if __name__ == '__main__':
    unittest.main()