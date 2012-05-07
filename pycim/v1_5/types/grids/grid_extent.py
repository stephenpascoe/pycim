"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.240465.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.



# Module exports.
__all__ = ['GridExtent']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.240465$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridExtent(object):
    """A class within the cim v1.5 type system.

    DataType for recording the geographic extent of a gridMosaic or gridTile.
    """
    def __init__(self):
        """Constructor"""
        super(GridExtent, self).__init__()

        self.__maximum_latitude = int()                             # type = int
        self.__maximum_longitude = int()                            # type = int
        self.__minimum_latitude = int()                             # type = int
        self.__minimum_longitude = int()                            # type = int
        self.__units = str()                                        # type = str


    @property
    def maximum_latitude(self):
        """Gets value of grid extent maximum_latitude property."""
        return self.__maximum_latitude

    @maximum_latitude.setter
    def maximum_latitude(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid extent maximum_latitude property."""
        self.__maximum_latitude = value

    @maximum_latitude.deleter
    def maximum_latitude(self, value):
        """Deletes grid extent maximum_latitude property."""
        raise TypeError("Cannot delete grid extent maximum_latitude property.")


    @property
    def maximum_longitude(self):
        """Gets value of grid extent maximum_longitude property."""
        return self.__maximum_longitude

    @maximum_longitude.setter
    def maximum_longitude(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid extent maximum_longitude property."""
        self.__maximum_longitude = value

    @maximum_longitude.deleter
    def maximum_longitude(self, value):
        """Deletes grid extent maximum_longitude property."""
        raise TypeError("Cannot delete grid extent maximum_longitude property.")


    @property
    def minimum_latitude(self):
        """Gets value of grid extent minimum_latitude property."""
        return self.__minimum_latitude

    @minimum_latitude.setter
    def minimum_latitude(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid extent minimum_latitude property."""
        self.__minimum_latitude = value

    @minimum_latitude.deleter
    def minimum_latitude(self, value):
        """Deletes grid extent minimum_latitude property."""
        raise TypeError("Cannot delete grid extent minimum_latitude property.")


    @property
    def minimum_longitude(self):
        """Gets value of grid extent minimum_longitude property."""
        return self.__minimum_longitude

    @minimum_longitude.setter
    def minimum_longitude(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid extent minimum_longitude property."""
        self.__minimum_longitude = value

    @minimum_longitude.deleter
    def minimum_longitude(self, value):
        """Deletes grid extent minimum_longitude property."""
        raise TypeError("Cannot delete grid extent minimum_longitude property.")


    @property
    def units(self):
        """Gets value of {class-name} units property."""
        return self.__units

    @units.setter
    def units(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} units property."""
        self.__units = value

    @units.deleter
    def units(self, value):
        """Deletes {class-name} units property."""
        raise TypeError("Cannot delete {class-name} units property.")



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
        append(d, 'maximum_latitude', self.__maximum_latitude, False, True, False)
        append(d, 'maximum_longitude', self.__maximum_longitude, False, True, False)
        append(d, 'minimum_latitude', self.__minimum_latitude, False, True, False)
        append(d, 'minimum_longitude', self.__minimum_longitude, False, True, False)
        append(d, 'units', self.__units, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridExtent()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridExtent', e)
