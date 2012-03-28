"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 16:29:10.803256.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.grids.grid_property import GridProperty



# Module exports.
__all__ = ['GridTileResolutionType']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 16:29:10.803256$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridTileResolutionType(object):
    """A class within the cim v1.5 type system.

    Provides a description and set of named properties for the horizontal or vertical resolution.
    """
    def __init__(self):
        """Constructor"""
        super(GridTileResolutionType, self).__init__()

        self.__description = str()                                  # type = str
        self.__properties = []                                      # type = grids.GridProperty


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A description of the resolution."""
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
    def properties(self):
        """Gets value of {class-name} properties property."""
        return list(self.__properties)

    @properties.setter
    def properties(self, value):
        """Sets value of {class-name} properties property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__properties = []
        for i in value:
            self.append_to_properties(i)

    @properties.deleter
    def properties(self, value):
        """Deletes {class-name} properties property."""
        raise TypeError("Cannot delete {class-name} properties property.")

    def append_to_properties(self, item):
        """Appends an item to the managed {class-name} properties collection."""
        if not isinstance(item, GridProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.append(item)

    def remove_from_properties(self, item):
        """Removes an item from the managed {class-name} properties collection."""
        if not isinstance(item, GridProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.remove(item)



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
        append(d, 'properties', self.__properties, True, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridTileResolutionType()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridTileResolutionType', e)
