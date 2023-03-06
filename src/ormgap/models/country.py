from mongoengine import Document, StringField

class Country(Document):

    """
    Represents a country in the database.

    Attributes:
    ----------
    iso_2: str
        Two-letter ISO code for the country (ISO 3166-1 alpha-2). Mandatory and unique.
    name: str
        Name of the country. Mandatory.

    Methods:
    -------
    save()
        Saves the Country object to the database.
    delete()
        Deletes the Country object from the database.
    """
    
    meta = {
        'collection': 'country'
    }
    iso_2 = StringField(max_length=2, unique=True, required=True)
    name = StringField(max_length=150, required=True)