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

echo "{% block vector_layers %}

	<script type='text/javascript' src='https://cdnjs.cloudflare.com/ajax/libs/randomcolor/0.5.4/randomColor.min.js'></script>


<script>

///////////////////////////
////// Vector Layers //////
///////////////////////////

    function popupFunc(feature, layer) {
            var popupContent = '';
            for (var k in feature.properties) {
                     var v = String(feature.properties[k]);
                     popupContent += '<strong>' + k + '</strong>' + ': ' + v + '</br>';
            };
            return layer.bindPopup(popupContent);
    };

    function rndmPolys(feature) {
	    var col = randomColor()
	    return {color: col,
		    weight: 3 };
    };

    function stylePolys(feature, prop) {
	    d = feature.properties.get(prop);
	    return d == 'ST. MARYS DRAINAGE BASIN' ? {color: '#00FF7F', opacity: 0.7}:
		    {color: '#ffffff', opacity: 1};
    };

    var baseVectorURL = 'http://216.218.220.139:8081/geoserver/iltf/ows?service=WFS&version=1.1.0&request=GetFeature&srsName=EPSG:4326&outputFormat=json&format_options=callback:loadGeoJson'

    var buff_bndry = new L.GeoJSON.AJAX(baseVectorURL + '&typeName=iltf:${TRIBE}_buff_bndry', {
        style: {clickable: true,
                fill: true,
		opacity: 0,
                fillOpacity: 0,
                zIndex: -100,
            },
    });


" > ../${TRIBE}/templates/${TRIBE}/${TRIBE}_vector_layers.html

for i in "${MODELS[@]}"; do

    echo "    var ${i} = new L.GeoJSON.AJAX(baseVectorURL + '&typeName=iltf:${TRIBE}_${i}', {
        style: {clickable: false,
                weight: 3,
	        color: '#000000',
	        fill: true,
	    },
	onEachFeature: popupFunc
    });
" >> ../$TRIBE/templates/$TRIBE/${TRIBE}_vector_layers.html

done

echo '

////////////////////////////
////// Leaflet Map /////////
////////////////////////////

    map.setView(new L.LatLng(46.4188, -84.4149), 11);
    map.addLayer(boundary);

</script>

{% endblock vector_layers %}' >> ../$TRIBE/templates/$TRIBE/${TRIBE}_vector_layers.html
