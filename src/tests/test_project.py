import unittest
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from mongoengine import connect, disconnect
from ormgap.models.project import Project

class ProjectTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Connect to a mock MongoDB instance. """
        connect('test_gap_analysis', host='mongomock://localhost')

    def setUp(self):
        """ Clean up the database before each test. """
        Project.objects.delete()
        self.project = Project(ext_id='P001', name='Test Project')
    
    def test_create_project(self):
        """ Test if a project is created successfully. """
        self.project.save()
        self.assertIsNotNone(self.project.id)
    
    def test_duplicate_ext_id(self):
        """ Test that a project with duplicate ext_id is not allowed. """
        self.project.save()
        duplicate_project = Project(ext_id='P001', name='Duplicate Project')
        with self.assertRaises(Exception) as context:
            duplicate_project.save()
        self.assertTrue('E11000 Duplicate Key Error' in str(context.exception))

    def test_get_project_by_ext_id(self):
        """ Test retrieving a project by ext_id. """
        self.project.save()
        project = Project.objects(ext_id='P001').first()
        self.assertIsNotNone(project)
        self.assertEqual(project.name, 'Test Project')

    def test_update_project_name(self):
        """ Test updating the project's name. """
        self.project.save()
        self.project.name = 'Updated Project'
        self.project.save()

        updated_project = Project.objects(ext_id='P001').first()
        self.assertEqual(updated_project.name, 'Updated Project')

    def test_delete_project(self):
        """ Test deleting a project. """
        self.project.save()
        self.project.delete()

        project = Project.objects(ext_id='P001').first()
        self.assertIsNone(project)

    @classmethod
    def tearDownClass(cls):
        """ Disconnect the mock database after all tests. """
        disconnect()

if __name__ == '__main__':
    unittest.main()
