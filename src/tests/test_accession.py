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

    def tearDown(self):
        self.crop.delete()
        self.group.delete()
        Accession.objects.delete()

if __name__ == '__main__':
    unittest.main()