from mongoengine import Document, StringField, ReferenceField, FloatField, DictField
from .crop import Crop
from .group import Group

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
    latitude: float
        Latitude of the geographical location where the accession was collected. Mandatory.
    longitude: float
        Longitude of the geographical location where the accession was collected. Mandatory.
    accession_id: str
        Unique identifier of the accession. Optional.
    other_attributes: dict
        Additional attributes of the accession. Optional.
    
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
    landrace_group = ReferenceField(Group, required=True)
    institution_name = StringField(max_length=255)
    source_database = StringField(max_length=255)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    accession_id = StringField(max_length=255)
    other_attributes = DictField()