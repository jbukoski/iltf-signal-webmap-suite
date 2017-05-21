from wms.maps import WmsMap
from wmslayers import testRaster

class testMap(WmsMap):
    layer_classes = [testRaster]
