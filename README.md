# Source Code for the GeoDjango based ILTF webmaps
## Product of SIG-NAL, Inc.
### Primary authors: Jacob J. Bukoski & Oliver Muellerklein

#### Packages necessary on Dukono

To be installed with 'apt':

  1. python3.4-dev
  2. python-psycopg2
  3. libpq-dev
  4. postgis&ast;

To be installed with 'pip':

  1. django
  2. django-geojson
  3. django-leaflet
  4. psycopg2
  5. mod-wsgi
  6. django-raster (gave issues)
  7. django-wms

#### Installation instructions:

  1. Install all necessary packages and modules
  2. Dump and create database (if necessary)
        ```
            $ psql -U postgres
            # CREATE DATABASE iltf;
            # CREATE EXTENSION postgis;
            # CREATE EXTENSION postgis_topology;
            # \q
            $ psql iltf < iltf.sql
        ```
  3. Create database **(This may be old / need to be deleted)**
    - -U postgres, adjusted password permissions to 'sig_pass'
  4. `python manage.py makemigrations`
  5. `python manage.py migrate`
  6. Load data to database

#### Start app

```
    $ python manage.py runserver
```

or

```
    $ ./manage.py runserver
```

#### File upload

Need to add the following to **settings.py**:

```
    # Media files

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
```

Need to add the following to **models.py**:

```
    from django.db import models
    
    class Document(models.Model):
        docfile = models.FileField(upload_to='documents/')
```

<hr>

TO DO:

  - Finalize carbon data layers to add
  - Build out legend function for raster layers
  - Build in transparency function
  - Build summary functions using draw function
  - Login functions on home page
  - Set-up in deployable, generalizable fashion
  - On import-map
    - allow user-specified name of layer
    - resolve blank map on delete (?)
    - checks for file type and size
