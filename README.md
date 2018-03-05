# Source Code for the GeoDjango based ILTF webmaps
## Product of SIG-NAL, Inc.
### Primary authors: Jacob J. Bukoski & Oliver Muellerklein


#### Webmap suite structure

The ILTF WebMap Suite is built with the GeoDjango python webmapping framework, leaflet visualizations, and a PostGIS backend. The current structure of the suite of webmaps is as follows:

- iltf (project directory)
  - manage.py
  - README.md (this file)
  - iltf (project level specifications)
    - ...
  - data (data directory)
    - ...
  - static (static library files)
    - ...
  - media (uploaded layers)
    - ...
  - calc (raster models and functions; considered an "app")
    - ...
  - tribe level apps... (e.g., comanche, lbst, tamaya)
    - ... (tribe-level specifications for individual webmaps)

#### Setting up a server or local machine for development/deployment

Packages necessary on Dukono

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

#### Start / stop / restart PostGreSQL

Potential error can occur if PostGreSQL cannot connect to its server (should be connecting to port 5432). In this case you can try to start, stop, or restart the server.   

*Start*

```
    $ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
```

*Stop*

```
    $ pg_ctl -D /usr/local/var/postgres stop -s -m fast
```


*Restart*

```
    $ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log restart
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

  - Build in transparency function
  - Set-up in deployable, generalizable fashion
  - Connect/set-up SIG VPN
  - Login functions
  - Watch video and connect with Shane
  - GEE integration?
  - Scale-invariant UI
