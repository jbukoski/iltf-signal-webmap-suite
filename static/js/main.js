
    var map, parcelSearch = [];

    $(document).ready(function() {
        $("[rel=tooltip]").tooltip();
        if (document.body.clientWidth <= 767) {
            $("#map").css("class", "col-sm-12 col-lg-12");
            $("#sidebar").css("display", "none");
        };
    });

    $(window).resize(function() {
        $(".tt-dropdown-menu").css("max-height", $("#container").height()-$(".navbar").height()-20);
        if (document.body.clientWidth <= 767) {
            $("#map").css("class", "col-sm-12 col-lg-12");
            $("#sidebar").css("display", "none");
        } else {
            $("#map").css("class", "col-sm-9 col-lg-9");
            $("#sidebar").css("display", "block");
        };
    });

    $("#toggle").click(function() {
        $("#toggle i").toggleClass("fa fa-check-square-o fa fa-map-marker");
        $("#map").toggleClass("col-sm-9 col-lg-9 col-sm-12 col-lg-12");
        $("#sidebar").toggle();
        if (document.body.clientWidth <= 767) {
            $("#map").toggle();
        };
        map.invalidateSize();
        return false;
    });
    //following script from;  https://gist.github.com/bmcbride/6186672
    $("input[name='basemapLayers']").change(function () {
        // Remove unchecked layers
        $("input:radio[name='basemapLayers']:not(:checked)").each(function () {
            map.removeLayer(window[$(this).attr("id")]);
        });
        // Add checked layer
        $("input:radio[name='basemapLayers']:checked").each(function () {
            map.addLayer(window[$(this).attr("id")]);
        });
    });

    $("input:checkbox[name='overlayLayers']").change(function () {
        var layers = [];
        function sortByKey(array, key) {
            return array.sort(function (a, b) {
                var x = a[key];
                var y = b[key];
                return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }
        if ($("#" + $(this).attr("id")).is(":checked")) {
            $("input:checkbox[name='overlayLayers']").each(function () {
                // Remove all overlay layers
                map.removeLayer(window[$(this).attr("id")]);
                if ($("#" + $(this).attr("id")).is(":checked")) {
                    // Add checked layers to array for sorting
                    layers.push({
                        "z-index": $(this).attr("z-index"),
                        "layer": $(this)
                    });
                }
            });
            // Sort layers array by z-index
            var orderedLayers = sortByKey(layers, "z-index");
            // Loop through ordered layers array and add to map in correct order
            $.each(orderedLayers, function () {
                map.addLayer(window[$(this)[0].layer[0].id]);
            });
        } else {
            // Simply remove unchecked layers
            map.removeLayer(window[$(this).attr("id")]);
        }
    });

////////////////////////////
////// Basemap Layers //////
////////////////////////////

    var api_key = 'pk.eyJ1IjoiZGlnaXRhbGdsb2JlIiwiYSI6ImNpcXE5ZjRxeDAyaHJmdm5oc20xbzVndGoifQ.jWIT7A205HVSAxKvVLeywQ';
    var hybrid = new L.tileLayer('https://{s}.tiles.mapbox.com/v4/digitalglobe.nal0mpda/{z}/{x}/{y}.png?access_token=' + api_key, {
        maxZoom: 19,
        attribution: '(c) <a href="http://microsites.digitalglobe.com/interactive/basemap_vivid/">DigitalGlobe</a> , (c) OpenStreetMap, (c) Mapbox'
    });
    var recent = new L.tileLayer('https://{s}.tiles.mapbox.com/v4/digitalglobe.nal0g75k/{z}/{x}/{y}.png?access_token=' + api_key, {
        maxZoom: 19,
        attribution: '(c) <a href="http://microsites.digitalglobe.com/interactive/basemap_vivid/">DigitalGlobe</a>'
    });
    var topo = new L.TileLayer("http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}.png", {
        maxZoom: 19,
        attribution: 'Basemap Courtesy of <a href="http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer" target="_blank">ESRI</a>'
      });
    recent.setZIndex(8);


///////////////////////////////////////
////// Add Leaflet-Draw controls //////
///////////////////////////////////////

    // Initialize the FeatureGroup to store editable layers

    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);

    // Specify some custom options for the Drawing tools

	var drawOptions = {
	draw: {
		polygon: {
			showArea: true
			}
	},
	edit: {
		featureGroup: drawnItems
		}
	}

	// Initialize the draw control and pass it the FeatureGroup of editable layers
	var drawControl = new L.Control.Draw(drawOptions);
	
	map.addControl(drawControl);

	map.on('draw:created', function (e) {
	var type = e.layerType,
		layer = e.layer;

	if (type === 'marker') {
		layer.bindPopup('A popup!');
	}

	// Do whatever else you need to. (save to db, add to map etc)
	drawnItems.addLayer(layer);
	});

    // Add opacity controls

    var opacitySlider = new L.Control.opacitySlider();
    map.addControl(opacitySlider);

    //opacitySlider.setOpacityLayer(landfire)



// Larger screens get expanded layer control
    if (document.body.clientWidth <= 767) {
        var isCollapsed = true;
    } else {
        var isCollapsed = false;
    };

    // Highlight search box text on click
    $("#searchbox").click(function () {
        $(this).select();
    });

    // Typeahead search functionality
    $(document).one("ajaxStop", function() {
        $("#loading").hide();
        $("#searchbox").typeahead([{
            name: "HabitatLeases",
            local: habitatLeasesSearch,
            minLength: 2,
            header: "<h4 class='typeahead-header'>HabitatLeases</h4>"
        },]).on("typeahead:selected", function (obj, datum) {
            if (datum.layer === "HabitatLeases") {
                map.setView([datum.lat, datum.lng], 16);
                if (map._layers[datum.id]) {
                    map._layers[datum.id].openPopup();
                };
            };
            if (datum.layer === "Boroughs") {
                map.fitBounds(datum.bounds);
            };
            if (datum.layer === "Theaters") {
                if (!map.hasLayer(theaters)) {
                    map.addLayer(theaters);
                    $("#theaters").prop("checked", true);
                };
                map.setView([datum.lat, datum.lng], 17);
                if (map._layers[datum.id]) {
                    map._layers[datum.id].openPopup();
                };
            };
            if (datum.layer === "Museums") {
                if (!map.hasLayer(museums)) {
                    map.addLayer(museums);
                    $("#museums").prop("checked", true);
                };
                map.setView([datum.lat, datum.lng], 17);
                if (map._layers[datum.id]) {
                    map._layers[datum.id].openPopup();
                };
            };
            if (datum.layer === "GeoNames") {
                map.setView([datum.lat, datum.lng], 14);
            };
            if ($("#navbar-collapse").height() > 50) {
                $("#navbar-collapse").collapse("hide");
            };
        }).on("typeahead:initialized ", function () {
            $(".tt-dropdown-menu").css("max-height", 300);
        }).on("typeahead:opened", function () {
            $(".navbar-collapse.in").css("max-height", $(document).height()-$(".navbar-header").height());
            $(".navbar-collapse.in").css("height", $(document).height()-$(".navbar-header").height());
        }).on("typeahead:closed", function () {
            $(".navbar-collapse.in").css("max-height", "");
            $(".navbar-collapse.in").css("height", "");
        });
    });

    // Placeholder hack for IE
    if (navigator.appName == "Microsoft Internet Explorer") {
        $("input").each( function () {
            if ($(this).val() == "" && $(this).attr("placeholder") != "") {
                $(this).val($(this).attr("placeholder"));
                $(this).focus(function () {
                    if ($(this).val() == $(this).attr("placeholder")) $(this).val("");
                });
                $(this).blur(function () {
                    if ($(this).val() == "") $(this).val($(this).attr("placeholder"));
                });
            }
        });
    }

