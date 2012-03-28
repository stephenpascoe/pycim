"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.808014.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.software.spatial_regridding_dimension_type import SpatialRegriddingDimensionType
from pycim.v1_5.types.software.spatial_regridding_property import SpatialRegriddingProperty
from pycim.v1_5.types.software.spatial_regridding_standard_method_type import SpatialRegriddingStandardMethodType
from pycim.v1_5.types.software.spatial_regridding_user_method import SpatialRegriddingUserMethod



# Module exports.
__all__ = ['SpatialRegridding']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.808014$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SpatialRegridding(object):
    """A class within the cim v1.5 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.
    """
    def __init__(self):
        """Constructor"""
        super(SpatialRegridding, self).__init__()

        self.__dimension = None                                     # type = software.SpatialRegriddingDimensionType
        self.__properties = []                                      # type = software.SpatialRegriddingProperty
        self.__standard_method = None                               # type = software.SpatialRegriddingStandardMethodType
        self.__user_method = None                                   # type = software.SpatialRegriddingUserMethod


    @property
    def dimension(self):
        """Gets value of {class-name} dimension property."""
        return self.__dimension

    @dimension.setter
    def dimension(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} dimension property."""
        self.__dimension = value

    @dimension.deleter
    def dimension(self, value):
        """Deletes {class-name} dimension property."""
        raise TypeError("Cannot delete {class-name} dimension property.")


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
        if not isinstance(item, SpatialRegriddingProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.append(item)

    def remove_from_properties(self, item):
        """Removes an item from the managed {class-name} properties collection."""
        if not isinstance(item, SpatialRegriddingProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.remove(item)


    @property
    def standard_method(self):
        """Gets value of {class-name} standard_method property."""
        return self.__standard_method

    @standard_method.setter
    def standard_method(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} standard_method property."""
        self.__standard_method = value

    @standard_method.deleter
    def standard_method(self, value):
        """Deletes {class-name} standard_method property."""
        raise TypeError("Cannot delete {class-name} standard_method property.")


    @property
    def user_method(self):
        """Gets value of {class-name} user_method property."""
        return self.__user_method

    @user_method.setter
    def user_method(self, value):
        if value is not None and not isinstance(value, SpatialRegriddingUserMethod):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} user_method property."""
        self.__user_method = value

    @user_method.deleter
    def user_method(self, value):
        """Deletes {class-name} user_method property."""
        raise TypeError("Cannot delete {class-name} user_method property.")



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
        append(d, 'dimension', self.__dimension, False, False, True)
        append(d, 'properties', self.__properties, True, False, False)
        append(d, 'standard_method', self.__standard_method, False, False, True)
        append(d, 'user_method', self.__user_method, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = SpatialRegridding()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.SpatialRegridding', e)
