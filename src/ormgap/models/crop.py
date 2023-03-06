from mongoengine import Document, StringField

class Crop(Document):

    """
    Represents a crop in the database.

    Attributes:
    ----------
    ext_id: str
        External ID of the crop. Mandatory and unique.
    name: str
        Name of the crop. Mandatory.
    base_name: str
        Base name of the crop.
    app_name: str
        Application name of the crop. Mandatory.
        
    Methods:
    -------
    save()
        Saves the Crop object to the database.
    delete()
        Deletes the Crop object from the database.
    """

    meta = {
        'collection': 'crop'
    }
    ext_id = StringField(max_length=100, unique=True, required=True)
    name = StringField(max_length=150, required=True)
    base_name = StringField(max_length=100)
    app_name = StringField(max_length=150, required=True)