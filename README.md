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

#### Installation instructions:

  1. Install all necessary packages and modules
  2. Create database
    - -U postgres, adjusted password permissions to 'md5'
  3. `python manage.py makemigrations`
  4. `python manage.py migrate`
  5. Load data to database

TO DO:

  - Enable mod-wsgi and host development webmaps from server

