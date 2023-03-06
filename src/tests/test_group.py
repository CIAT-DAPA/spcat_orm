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

    def tearDown(self):
        self.crop.delete()
        Group.objects.delete()

    if __name__ == '__main__':
        unittest.main()