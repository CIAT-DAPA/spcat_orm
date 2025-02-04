from mongoengine import Document, StringField, ReferenceField, FloatField, DictField
from .crop import Crop
from .group import Group
from .country import Country
from .project import Project

class Accession(Document):

    """"
    Represents an accession in the database.

    Attributes:
    ----------
    species_name: str
        Name of the species of the accession. Optional.
    crop: Crop
        Crop object, Crop to which the accession belongs. Mandatory.
    landrace_group: Group
        Group object, Landrace group to which the accession belongs. Mandatory.
    institution_name: str
        Name of the institution that holds the accession. Optional.
    source_database: str
        Name of the database where the accession was originally stored. Optional.
    country: Country
        Country object, country to which the accession belongs. Mandatory.
    latitude: float
        Latitude of the geographical location where the accession was collected. Mandatory.
    longitude: float
        Longitude of the geographical location where the accession was collected. Mandatory.
    accession_id: str
        The identifier of the accession in source database. Optional.
    ext_id: str
        External identifier for the accession. Mandatory and unique.
    other_attributes: dict
        Additional attributes of the accession. Optional.
    project: Project
        Project object, project to which the accession is linked. Optional.    
    
    Methods:
    -------
    save()
        Saves the Accession object to the database.
    delete()
        Deletes the Accession object from the database.
    """

    meta = {
        'collection': 'accession'
    }
    species_name = StringField(max_length=150)
    crop = ReferenceField(Crop, required=True)
    landrace_group = ReferenceField(Group, required=False)
    institution_name = StringField(max_length=255)
    source_database = StringField(max_length=255)
    country = ReferenceField(Country, required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    accession_id = StringField(max_length=255)
    ext_id = StringField(max_length=255, required=True, unique=True)
    project = ReferenceField(Project, required=False)
    other_attributes = DictField()