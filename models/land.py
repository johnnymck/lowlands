"""Land.py
Land models and helpers for simulating land 'Physics'
"""

class LandTile(object):
    """Land is set at a height from -100 to 100, with water level averaging
    0 but dynamically changing
    """
    _height = 0
    _structure = None

    def __init__(self, height=0, structs=None):
        self._height = height
        self._structures = structs
    
    def rise(self, factor):
        self._height += factor
        if self._height > 100:
            self.height = 100
    
    def fall(self, factor):
        self._height -= factor
        if self._height < -100:
            self.height = -100
    
    def set_asset(self, asset):
        if self._structure == None:
            self._structure = asset
        else:
            raise Exception
    
    def get_asset(self):
        return self._structure