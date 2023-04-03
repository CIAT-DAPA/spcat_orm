# Gap Analysis ORM

![GitHub release (latest by date)](https://img.shields.io/github/v/release/CIAT-DAPA/spcat_orm) ![](https://img.shields.io/github/v/tag/CIAT-DAPA/spcat_orm)

This is an ORM (Object-Relational Mapping) that uses the Mongoengine library to interact with a MongoDB database. This ORM has been designed to handle information related to accessions, crop groups, crops and countries.

## Features

- Built using Mongoengine for MongoDB
- Supports Python 3.x

## Getting Started

To use this ORM, it is necessary to have an instance of MongoDB running.

### Prerequisites

- Python 3.x
- MongoDB

## Usage


This ORM can be used as a library in other Python projects. The models are located in the my_orm/models folder, and can be imported like any other Python module. To install this orm as a library you need to execute the following command:

````bash
pip install git+https://github.com/CIAT-DAPA/spcat_orm
````

If you want to download a specific version of orm you can do so by indicating the version tag (@v0.0.0) at the end of the install command 

````bash
pip install git+https://github.com/CIAT-DAPA/spcat_orm@v0.2.0
````

To interact with the database, it is necessary to connect the ORM to the MongoDB database. This can be done using the connect() function of the mongoengine library, as shown in the following example:

```python
from mongoengine import connect
from ormgap import *

# Connect to the database
connect(host='mongodb://localhost/gap_analysis')

# Perform database queries using the models defined in ormgap/models

# Query the Accession collection
accessions = Accession.objects(species_name='Solanum lycopersicum')

# Do something with the accessions
for accession in accessions:
    print(accession.id, accession.species_name, accession.crop)
```
## Models

### Country

Represents a country in the database.

Attributes:

- iso_2: `str` Two-letter ISO code for the country (ISO 3166-1 alpha-2). Mandatory and unique.
- name: `str` Name of the country. Mandatory.

### Crop

Represents a crop in the database.

Attributes:

- ext_id: `str` External ID of the crop. Mandatory and unique.
- name: `str` Name of the crop. Mandatory.
- base_name: `str` Base name of the crop.
- app_name: `str` Application name of the crop. Mandatory.

### Group

Represents a group in the database.

Attributes:

- group_name: `str` Name of the group. Mandatory.
- crop: `Crop` Crop object that the group belongs to. Mandatory.
- ext_id: `str` External identifier for the group. Mandatory and unique.
    

### Accession

Represents an accession in the database.

Attributes:

- species_name: `str` Name of the species of the accession. Optional.
- crop: `Crop` Crop object, Crop to which the accession belongs. Mandatory.
- landrace_group: `Group` Group object, Landrace group to which the accession belongs. Mandatory.
- country: `Country` Country object, country to which the accession belongs. Mandatory.
- institution_name: `str` Name of the institution that holds the accession. Optional.
- source_database: `str` Name of the database where the accession was originally stored. Optional.
- latitude: `float` Latitude of the geographical location where the accession was collected. Mandatory.
- longitude: `float` Longitude of the geographical location where the accession was collected. Mandatory.
- accession_id: `str` The identifier of the accession in source database. Optional.
- ext_id: `str` External identifier for the accession. Mandatory and unique.
- other_attributes: `dict` Additional attributes of the accession. Optional.