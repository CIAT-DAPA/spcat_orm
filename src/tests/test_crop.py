import unittest
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from mongoengine import connect
from ormgap.models.crop import Crop

class TestCrop(unittest.TestCase):

    def setUp(self):
        connect('test_gap_analysis', host='mongomock://localhost')
        self.crop = Crop(
            ext_id='1234',
            name='corn',
            base_name='zea_mays',
            app_name='Corn'
        )

    def test_create_crop(self):
        # Crea un nuevo crop
        
        self.crop.save()
        self.assertIsNotNone(self.crop.id)

        print(self.crop)

        # Verifica que el crop haya sido creado exitosamente
        crop = Crop.objects(id=self.crop.id).first()
        self.assertEqual(crop.ext_id, '1234')
        self.assertEqual(crop.name, 'corn')
        self.assertEqual(crop.base_name, 'zea_mays')
        self.assertEqual(crop.app_name, 'Corn')

    def tearDown(self):
        Crop.objects.delete()

    if __name__ == '__main__':
        unittest.main()