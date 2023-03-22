import unittest
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from mongoengine import connect
from ormgap.models.accession import Accession
from ormgap.models.crop import Crop
from ormgap.models.group import Group

class AccessionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect('test_gap_analysis', host='mongomock://localhost')

    def setUp(self):
        self.crop = Crop(name='Test Crop', base_name='Test Crop Base', app_name='Test Crop App', ext_id='1234').save()
        self.assertIsNotNone(self.crop.id)
        self.group = Group(group_name='Test Group', crop=self.crop, ext_id='12345').save()
        self.assertIsNotNone(self.group.id)
        self.accession = Accession(
            species_name='Test Species', 
            crop=self.crop, 
            landrace_group=self.group, 
            institution_name='ICARDA',
            source_database='GENESYS',
            latitude=40.7128,
            longitude=-74.0060,
            accession_id='12345',
            ext_id='123'
        )

    def test_create_accession(self):
        self.accession.save()
        print(self.accession)
        self.assertIsNotNone(self.accession.id)

        accession = Accession.objects(id=self.accession.id).first()
        self.assertEqual(accession.crop.id, self.crop.id)
        self.assertEqual(accession.landrace_group.id, self.group.id)
        self.assertEqual(accession.latitude, 40.7128)
        self.assertEqual(accession.longitude, -74.0060)

    
    def test_get_accession_by_crop(self):
        self.accession.save()
        accessions = Accession.objects(crop=self.crop)
        self.assertGreaterEqual(len(accessions), 1)
        accession = accessions.first()
        self.assertEqual(self.crop.id, accession.crop.id)

    def test_get_accession_by_group(self):
        self.accession.save()
        accessions =Accession.objects(landrace_group=self.group)
        self.assertGreaterEqual(len(accessions), 1)
        accession = accessions.first()
        self.assertEqual(self.group.id, accession.landrace_group.id)
    
    def test_unique_ext_id(self):
        self.accession.save()
        accession = Accession(
            species_name='Test Species',
            crop=self.crop,
            landrace_group=self.group,
            institution_name='ICARDA',
            source_database='GENESYS',
            latitude=91, # Latitud inválida
            longitude=-181, # Longitud inválida
            accession_id='12345',
            ext_id='123'
        )
        with self.assertRaises(Exception) as context:
            accession.save()
        print(str(context.exception))
        self.assertTrue('Tried to save duplicate unique keys (E11000 Duplicate Key Error)' in str(context.exception))

    def test_get_accession_by_invalid_id(self):
        # Busca un country por un ID que no existe
        found_country = Accession.objects(crop='609e996db1751152b09f5555').first()
        self.assertIsNone(found_country)

    def test_update_accession(self):
        self.accession.save()

        self.accession.species_name = 'New Species Name'
        self.accession.save()

        accession = Accession.objects(id=self.accession.id).first()
        self.assertEqual(accession.species_name, 'New Species Name')
    
    def test_delete_accession(self):
        self.accession.save()

        self.accession.delete()

        accession = Accession.objects(id=self.accession.id).first()
        self.assertIsNone(accession)

    def tearDown(self):
        self.crop.delete()
        self.group.delete()
        Accession.objects.delete()

if __name__ == '__main__':
    unittest.main()