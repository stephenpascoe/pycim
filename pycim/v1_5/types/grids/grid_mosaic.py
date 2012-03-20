"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-20 16:28:50.052123.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.



# Module exports.
__all__ = ['GridMosaic']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-20 16:28:50.052123$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridMosaic(object):
    """A class within the cim v1.5 type system.

    The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.
    """
    def __init__(self):
        """Constructor"""
        super(GridMosaic, self).__init__()

        self.__description = str()                                  # type = str
        self.__long_name = str()                                    # type = str
        self.__short_name = str()                                   # type = str


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of a grid mosaic."""
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
    def long_name(self):
        """Gets value of {class-name} long_name property.

        Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes."""
        return self.__long_name

    @long_name.setter
    def long_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} long_name property."""
        self.__long_name = value

    @long_name.deleter
    def long_name(self, value):
        """Deletes {class-name} long_name property."""
        raise TypeError("Cannot delete {class-name} long_name property.")


    @property
    def short_name(self):
        """Gets value of grid mosaic short_name property.

        Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. 'UM ATM N96'."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid mosaic short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes grid mosaic short_name property."""
        raise TypeError("Cannot delete grid mosaic short_name property.")



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
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridMosaic()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridMosaic', e)
