from mongoengine import Document, StringField, ReferenceField
from .crop import Crop

class Group(Document):

    """
    Represents a group in the database.

    Attributes:
    ----------
    group_name: str
        Name of the group. Mandatory.
    crop: Crop
        Crop object that the group belongs to. Mandatory.
    ext_id: str
        External identifier for the group. Mandatory and unique.
    
    Methods:
    -------
    save()
        Saves the Group object to the database.
    delete()
        Deletes the Group object from the database.
    """

    meta = {
        'collection': 'group'
    }
    group_name = StringField(max_length=255, required=True)
    crop = ReferenceField(Crop, required=True)
    ext_id = StringField(max_length=100, required=True, unique=True)