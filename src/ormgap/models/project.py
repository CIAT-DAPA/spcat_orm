from mongoengine import Document, StringField

class Project(Document):
    """
    Represents a project in the database.

    Attributes:
    ----------
    ext_id: str
        External identifier for the project. Mandatory and unique.
    name: str
        Name of the project. Mandatory.

    Methods:
    -------
    save()
        Saves the Project object to the database.
    delete()
        Deletes the Project object from the database.
    """

    meta = {
        'collection': 'project'
    }
    ext_id = StringField(max_length=100, unique=True, required=True)
    name = StringField(max_length=150, required=True)
