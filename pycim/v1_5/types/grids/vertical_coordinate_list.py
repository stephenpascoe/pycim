"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.733750.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.grids.coordinate_list import CoordinateList
from pycim.v1_5.types.grids.grid_property import GridProperty



# Module exports.
__all__ = ['VerticalCoordinateList']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.733750$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class VerticalCoordinateList(CoordinateList):
    """A class within the cim v1.5 type system.

    There are some specific attributes that are associated with vertical coordinates.
    """
    def __init__(self):
        """Constructor"""
        super(VerticalCoordinateList, self).__init__()

        self.__form = str()                                         # type = str
        self.__properties = []                                      # type = grids.GridProperty
        self.__type = str()                                         # type = str


    @property
    def form(self):
        """Gets value of {class-name} form property.

        Units of measure used by the coordinates."""
        return self.__form

    @form.setter
    def form(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} form property."""
        self.__form = value

    @form.deleter
    def form(self, value):
        """Deletes {class-name} form property."""
        raise TypeError("Cannot delete {class-name} form property.")


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


    @property
    def type(self):
        """Gets value of {class-name} type property.

        Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes {class-name} type property."""
        raise TypeError("Cannot delete {class-name} type property.")



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
        d = dict(super(VerticalCoordinateList, self).as_dict())
        append(d, 'form', self.__form, False, True, False)
        append(d, 'properties', self.__properties, True, False, False)
        append(d, 'type', self.__type, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = VerticalCoordinateList()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.VerticalCoordinateList', e)
