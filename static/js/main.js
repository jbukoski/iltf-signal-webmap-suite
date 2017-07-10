
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
    var esriWorld = new L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 19,
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
    });
    var osmBaseMap = new L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });
    var topo = new L.TileLayer("http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}.png", {
        maxZoom: 19,
        attribution: 'Basemap Courtesy of <a href="http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer" target="_blank">ESRI</a>'
      });

// Larger screens get expanded layer control
    if (document.body.clientWidth <= 767) {
        var isCollapsed = true;
    } else {
        var isCollapsed = false;
    };

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

