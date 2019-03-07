#!/bin/sh

TRIBE=$1

echo $'from django.contrib.gis.db import models' > ../$TRIBE/models.py

echo $'import os
from django.contrib.gis.utils import LayerMapping
from . import models\n' > ../$TRIBE/load.py

echo "Writing models.py file..."

for FILE in ../data/$TRIBE/*.shp; do

FILENAME=${FILE#../data/$TRIBE/}
FILENAME=${FILENAME%.shp}

OGR_OUT="$(../manage.py ogrinspect $FILE $FILENAME --srid 4326 --multi --mapping)"

MODELS_NUM="$(echo "$OGR_OUT" | grep -n '    geom = models.' | cut -f1 -d:)"
MAPPING_NUM="$(echo "$OGR_OUT" | grep -n $FILENAME"_mapping" | cut -f1 -d:)"


# Print text to models.py

MODELS="$(echo "$OGR_OUT" | sed -n '3,'"$MODELS_NUM"'p')"

echo "$MODELS" >> ../$TRIBE/models.py

echo $'    id = models.AutoField(primary_key = True)\n
    def __str__(self):
        return \'%s\' % (self.id)\n'   >> ../$TRIBE/models.py

# Print mapping to load.py

MAPPING="$(echo "$OGR_OUT" | sed -n "$MAPPING_NUM"',$p')"

echo "$MAPPING" >> ../$TRIBE/load.py

echo -en '\n' >> ../$TRIBE/load.py

echo "${FILENAME}_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', '$TRIBE', '${FILENAME}.shp'))" >> ../$TRIBE/load.py

echo -en '\n' >> ../$TRIBE/load.py

done

echo "def run(verbose=True):" >> ../$TRIBE/load.py

echo "Writing load.py file..."

for FILE in ../data/$TRIBE/*.shp; do

FILENAME=${FILE#../data/$TRIBE/}
FILENAME=${FILENAME%.shp}

echo -en '\n' >> ../$TRIBE/load.py

echo "    ${FILENAME}_lm = LayerMapping(
        models.${FILENAME}, ${FILENAME}_shp, ${FILENAME}_mapping,
        transform=False, encoding='iso-8859-1'
    )
    ${FILENAME}_lm.save(strict=True, verbose=verbose)" >> ../$TRIBE/load.py

done

echo "

#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='$TRIBE/uploaded')"    >> ../$TRIBE/models.py


echo "Done."
