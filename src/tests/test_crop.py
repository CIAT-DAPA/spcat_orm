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

    def test_create_duplicate_crop(self):
        self.crop.save()
        crop2 = Crop(
            ext_id='1234',
            name='wheat',
            base_name='triticum_aestivum',
            app_name='Wheat'
        )

        with self.assertRaises(Exception) as context:
            crop2.save()
        
        print(str(context.exception))
        self.assertTrue('Tried to save duplicate unique keys (E11000 Duplicate Key Error)' in str(context.exception))

    def test_get_crop_by_invalid_id(self):
        # Busca un country por un ID que no existe
        found_country = Crop.objects(id='609e996db1751152b09f5555').first()
        self.assertIsNone(found_country)
    
    def test_update_crop(self):
        self.crop.save()

        self.crop.name = 'maize'
        self.crop.base_name = 'zea_mays_subsp_mays'
        self.crop.app_name = 'Maize'
        self.crop.save()

        crop = Crop.objects(id=self.crop.id).first()
        self.assertEqual(crop.ext_id, '1234')
        self.assertEqual(crop.name, 'maize')
        self.assertEqual(crop.base_name, 'zea_mays_subsp_mays')
        self.assertEqual(crop.app_name, 'Maize')
    
    def test_delete_crop(self):
        self.crop.save()

        self.crop.delete()
        crop = Crop.objects(id=self.crop.id).first()

        self.assertIsNone(crop)

    def tearDown(self):
        Crop.objects.delete()

    if __name__ == '__main__':
        unittest.main()