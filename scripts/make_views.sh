#!/bin/sh

TRIBE=$1

sed -i 's/RENAME/bmic/g' ../$TRIBE/views.py

PY_MODELS=($(python ../manage.py shell -c " 

from django.apps import apps

mdl_dct = {}

for model in apps.all_models['$TRIBE']:
    fields = []
    fields = [ i.get_attname() for i in apps.all_models['$TRIBE'][model]._meta.get_fields() ]
    mdl_dct[apps.all_models['$TRIBE'][model]._meta.model_name] = fields

file = open('vals.txt', 'w')

for i in mdl_dct:
    val_str = str( i + ' \'' + '\',\''.join(mdl_dct[i]) + '\'' + '\n')
    file.write(val_str)

file.close()

"))

# Convert to bash array and write to the python file

declare -A fields

while IFS=" " read -r key value ; do
    fields["$key"]="$value"
done < vals.txt


# Write out the views file

echo -e "\n## Layer Views\n" >> ../$TRIBE/views.py


for i in "${!fields[@]}"; do

    echo -e "def ${i}_view(request):
    ${i}_json = serialize('geojson', models.${i}.objects.all(), geometry_field='geom', fields = ($(sed 's/geom, //g' <<< "$(sed 's/,/, /g' <<< "${fields[$i]}")")))
    return HttpResponse(${i}_json, content_type='json')\n" >> ../$TRIBE/views.py

done

echo -e "## Layer Download Views\n" >> ../$TRIBE/views.py

for i in "${!fields[@]}"; do

    echo -e "def ${i}_view_dl(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', '$TRIBE', '${i}.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=\"${i}.zip\"'

    return response\n  " >> ../$TRIBE/views.py

done
