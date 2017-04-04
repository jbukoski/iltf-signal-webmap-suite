# Source Code for the GeoDjango based ILTF webmaps
## Product of SIG-NAL, Inc.
### Primary author: Jacob J. Bukoski

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

TO DO:

  - ~~Styling and popup content~~
  - Build Raster models
  - Vector Slicing for faster display of geojson layers
   - From GeoDjango framework?
  - Add in other layers
  - Set up as deployable app
  - Build user adjustable layers
  - Change background map in Admin page
  - Deploy to SIG server
