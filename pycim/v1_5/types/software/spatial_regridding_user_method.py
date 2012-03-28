"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 16:29:10.871046.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.data.data_object import DataObject
from pycim.v1_5.types.shared.cim_reference import CimReference



# Module exports.
__all__ = ['SpatialRegriddingUserMethod']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 16:29:10.871046$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SpatialRegriddingUserMethod(object):
    """A class within the cim v1.5 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.
    """
    def __init__(self):
        """Constructor"""
        super(SpatialRegriddingUserMethod, self).__init__()

        self.__file = None                                          # type = data.DataObject
        self.__file_reference = None                                # type = shared.CimReference
        self.__name = str()                                         # type = str


    @property
    def file(self):
        """Gets value of {class-name} file property."""
        return self.__file

    @file.setter
    def file(self, value):
        if value is not None and not isinstance(value, DataObject):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} file property."""
        self.__file = value

    @file.deleter
    def file(self, value):
        """Deletes {class-name} file property."""
        raise TypeError("Cannot delete {class-name} file property.")


    @property
    def file_reference(self):
        """Gets value of {class-name} file_reference property."""
        return self.__file_reference

    @file_reference.setter
    def file_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} file_reference property."""
        self.__file_reference = value

    @file_reference.deleter
    def file_reference(self, value):
        """Deletes {class-name} file_reference property."""
        raise TypeError("Cannot delete {class-name} file_reference property.")


    @property
    def name(self):
        """Gets value of spatial regridding user method name property."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of spatial regridding user method name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes spatial regridding user method name property."""
        raise TypeError("Cannot delete spatial regridding user method name property.")



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
        append(d, 'file', self.__file, False, False, False)
        append(d, 'file_reference', self.__file_reference, False, False, False)
        append(d, 'name', self.__name, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = SpatialRegriddingUserMethod()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.SpatialRegriddingUserMethod', e)
