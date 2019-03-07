#!/bin/sh

TRIBE=$1

# Generate model-specific URLs

PY_MODELS=$(python ../manage.py shell -c "

from django.apps import apps
from django.contrib import admin

mods = apps.all_models['$TRIBE']

empty = ''
for i in mods.keys():
    empty += i+' '

print(empty)

")

# Convert to bash array and write to the html file

MODELS=( $PY_MODELS )

# Write layers file

echo '{% block layers %}

<script>

///////////////////////////
////// Vector Layers //////
///////////////////////////

            function popupFunc(feature, layer) {
                var popupContent = "";
                for (var k in feature.properties) {
                     var v = String(feature.properties[k]);
                     popupContent += "<strong>" + k + "</strong>" + ": " + v + "</br>";
                };
                return layer.bindPopup(popupContent);
            };

    var buff_bndry = new L.GeoJSON.AJAX('{% url \"${TRIBE}_buff_bndry\" %}', {
        style: {clickable: true,
                fill: true,
		fillOpacity: 0,
		opacity: 0,
		zIndex: -100,
            },
    });



' > ../${TRIBE}/templates/${TRIBE}/layers.html

for i in "${MODELS[@]}"; do

    echo "    var ${i} = new L.GeoJSON.AJAX('{% url \"${TRIBE}_${i}\" %}', {
        style: {clickable: false,
                weight: 3,
	        color: '#000000',
	        fill: true,
	    },
	onEachFeature: popupFunc
    });
" >> ../$TRIBE/templates/$TRIBE/layers.html

done

echo '

////////////////////////////
////// Leaflet Map /////////
////////////////////////////

    map.setView(new L.LatLng(46.4188, -84.4149), 11);
    map.addLayer(boundary);

</script>

{% endblock layers %}' >> ../$TRIBE/templates/$TRIBE/layers.html
