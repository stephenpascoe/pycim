"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.239112.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.



# Module exports.
__all__ = ['CoordinateList']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.239112$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CoordinateList(object):
    """A class within the cim v1.5 type system.

    The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.
    """
    def __init__(self):
        """Constructor"""
        super(CoordinateList, self).__init__()

        self.__has_constant_offset = bool()                         # type = bool
        self.__length = int()                                       # type = int
        self.__uom = str()                                          # type = str


    @property
    def has_constant_offset(self):
        """Gets value of {class-name} has_constant_offset property.

        Set to true if coordinates in the built array have constant offset."""
        return self.__has_constant_offset

    @has_constant_offset.setter
    def has_constant_offset(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} has_constant_offset property."""
        self.__has_constant_offset = value

    @has_constant_offset.deleter
    def has_constant_offset(self, value):
        """Deletes {class-name} has_constant_offset property."""
        raise TypeError("Cannot delete {class-name} has_constant_offset property.")


    @property
    def length(self):
        """Gets value of {class-name} length property.

        Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used."""
        return self.__length

    @length.setter
    def length(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} length property."""
        self.__length = value

    @length.deleter
    def length(self, value):
        """Deletes {class-name} length property."""
        raise TypeError("Cannot delete {class-name} length property.")


    @property
    def uom(self):
        """Gets value of {class-name} uom property.

        Units of measure used by the coordinates."""
        return self.__uom

    @uom.setter
    def uom(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} uom property."""
        self.__uom = value

    @uom.deleter
    def uom(self, value):
        """Deletes {class-name} uom property."""
        raise TypeError("Cannot delete {class-name} uom property.")



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
        append(d, 'has_constant_offset', self.__has_constant_offset, False, True, False)
        append(d, 'length', self.__length, False, True, False)
        append(d, 'uom', self.__uom, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = CoordinateList()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.CoordinateList', e)
