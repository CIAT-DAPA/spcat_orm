import unittest
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from mongoengine import connect
from ormgap.models.group import Group
from ormgap.models.crop import Crop

class TestGroup(unittest.TestCase):
    def setUp(self):
        connect('test_gap_analysis', host='mongomock://localhost')
        self.crop = Crop(name='Test Crop', base_name='Test Crop Base', app_name='Test Crop App', ext_id='1234' ).save()
        self.assertIsNotNone(self.crop.id)
        self.group = Group(
            group_name='Landraces of corn',
            crop=self.crop,
            ext_id='1234'
        )

    def test_create_group(self):
        self.group.save()
        self.assertIsNotNone(self.group.id)

        group = Group.objects(id=self.group.id).first()
        print(group)
        self.assertEqual(group.group_name, 'Landraces of corn')
        self.assertEqual(group.crop, self.crop)        
        self.assertEqual(group.ext_id, '1234')

    def test_create_duplicate_group(self):
        # Intenta crear un grupo con el mismo ext_id que otro grupo existente
        self.group.save()
        group2 = Group(
            group_name='Modern corn hybrids',
            crop=self.crop,
            ext_id='1234'
        )
        with self.assertRaises(Exception) as context:
            group2.save()
        
        print(str(context.exception))
        self.assertTrue('Tried to save duplicate unique keys (E11000 Duplicate Key Error)' in str(context.exception))

    def test_create_group_without_crop(self):
        # Intenta crear un grupo sin el objeto Crop
        group2 = Group(
            group_name='Landraces of corn',
            ext_id='5678'
        )
        with self.assertRaises(Exception) as context:
            group2.save()
            
        print(str(context.exception))
        self.assertTrue("ValidationError (Group:None) (Field is required: ['crop'])" in str(context.exception))

    def test_delete_group(self):
        self.group.save()

        self.group.delete()
        group = Group.objects(id=self.group.id).first()

        self.assertIsNone(group)

    def test_get_country_by_invalid_id(self):
        # Busca un country por un ID que no existe
        found_country = Group.objects(crop='609e996db1751152b09f5555').first()
        self.assertIsNone(found_country)

    def tearDown(self):
        self.crop.delete()
        Group.objects.delete()

    if __name__ == '__main__':
        unittest.main()