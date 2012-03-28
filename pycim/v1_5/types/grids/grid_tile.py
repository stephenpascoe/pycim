"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.730701.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.grids.grid_extent import GridExtent
from pycim.v1_5.types.grids.grid_tile_resolution_type import GridTileResolutionType
from pycim.v1_5.types.grids.vertical_coordinate_list import VerticalCoordinateList



# Module exports.
__all__ = ['GridTile']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.730701$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridTile(object):
    """A class within the cim v1.5 type system.

    The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.
    """
    def __init__(self):
        """Constructor"""
        super(GridTile, self).__init__()

        self.__description = str()                                  # type = str
        self.__extent = None                                        # type = grids.GridExtent
        self.__horizontal_resolution = None                         # type = grids.GridTileResolutionType
        self.__mnemonic = str()                                     # type = str
        self.__vertical_resolution = None                           # type = grids.GridTileResolutionType
        self.__zcoords = None                                       # type = grids.VerticalCoordinateList


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of a grid tile."""
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} description property."""
        self.__description = value

    @description.deleter
    def description(self, value):
        """Deletes {class-name} description property."""
        raise TypeError("Cannot delete {class-name} description property.")


    @property
    def extent(self):
        """Gets value of {class-name} extent property."""
        return self.__extent

    @extent.setter
    def extent(self, value):
        if value is not None and not isinstance(value, GridExtent):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} extent property."""
        self.__extent = value

    @extent.deleter
    def extent(self, value):
        """Deletes {class-name} extent property."""
        raise TypeError("Cannot delete {class-name} extent property.")


    @property
    def horizontal_resolution(self):
        """Gets value of {class-name} horizontal_resolution property.

        Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch)."""
        return self.__horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, value):
        if value is not None and not isinstance(value, GridTileResolutionType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} horizontal_resolution property."""
        self.__horizontal_resolution = value

    @horizontal_resolution.deleter
    def horizontal_resolution(self, value):
        """Deletes {class-name} horizontal_resolution property."""
        raise TypeError("Cannot delete {class-name} horizontal_resolution property.")


    @property
    def mnemonic(self):
        """Gets value of {class-name} mnemonic property."""
        return self.__mnemonic

    @mnemonic.setter
    def mnemonic(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} mnemonic property."""
        self.__mnemonic = value

    @mnemonic.deleter
    def mnemonic(self, value):
        """Deletes {class-name} mnemonic property."""
        raise TypeError("Cannot delete {class-name} mnemonic property.")


    @property
    def vertical_resolution(self):
        """Gets value of {class-name} vertical_resolution property.

        Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property)."""
        return self.__vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, value):
        if value is not None and not isinstance(value, GridTileResolutionType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} vertical_resolution property."""
        self.__vertical_resolution = value

    @vertical_resolution.deleter
    def vertical_resolution(self, value):
        """Deletes {class-name} vertical_resolution property."""
        raise TypeError("Cannot delete {class-name} vertical_resolution property.")


    @property
    def zcoords(self):
        """Gets value of {class-name} zcoords property.

        This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods."""
        return self.__zcoords

    @zcoords.setter
    def zcoords(self, value):
        if value is not None and not isinstance(value, VerticalCoordinateList):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} zcoords property."""
        self.__zcoords = value

    @zcoords.deleter
    def zcoords(self, value):
        """Deletes {class-name} zcoords property."""
        raise TypeError("Cannot delete {class-name} zcoords property.")



    def as_dict(self):
        """Gets dictionary representation of self used to create other representations such as json, xml ...etc.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'description', self.__description, False, True, False)
        append(d, 'extent', self.__extent, False, False, False)
        append(d, 'horizontal_resolution', self.__horizontal_resolution, False, False, False)
        append(d, 'mnemonic', self.__mnemonic, False, True, False)
        append(d, 'vertical_resolution', self.__vertical_resolution, False, False, False)
        append(d, 'zcoords', self.__zcoords, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridTile()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridTile', e)
