from wms.views import WmsView
from wms.wmsmaps import testMap

class testView(WmsView):
    map_class = testMap
