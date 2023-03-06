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

## Installation

To use this ORM, it is necessary to have an instance of MongoDB running. It is also recommended to create a virtual environment to work with this project and make sure that the dependencies are installed in the virtual environment instead of the global system.

1. Clone the repository
````sh
git clone https://github.com/your_username_/Project-Name.git
````

2. Create a virtual environment
````sh
python3 -m venv env
````
3. Activate the virtual environment
````sh
source env/bin/activate
````
4. Install the required packages
````sh
pip install -r requirements.txt
````

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
