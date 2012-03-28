"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 16:29:10.796694.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.cim_info import CimInfo
from pycim.v1_5.types.grids.grid_mosaic import GridMosaic



# Module exports.
__all__ = ['GridSpec']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 16:29:10.796694$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridSpec(object):
    """A class within the cim v1.5 type system.

    This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.
    """
    def __init__(self):
        """Constructor"""
        super(GridSpec, self).__init__()

        self.__cim_info = None                                      # type = shared.CimInfo
        self.__esm_exchange_grids = []                              # type = grids.GridMosaic
        self.__esm_model_grids = []                                 # type = grids.GridMosaic


    @property
    def cim_info(self):
        """Gets value of grid spec cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid spec cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes grid spec cim_info property."""
        raise TypeError("Cannot delete grid spec cim_info property.")


    @property
    def esm_exchange_grids(self):
        """Gets value of {class-name} esm_exchange_grids property."""
        return list(self.__esm_exchange_grids)

    @esm_exchange_grids.setter
    def esm_exchange_grids(self, value):
        """Sets value of {class-name} esm_exchange_grids property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__esm_exchange_grids = []
        for i in value:
            self.append_to_esm_exchange_grids(i)

    @esm_exchange_grids.deleter
    def esm_exchange_grids(self, value):
        """Deletes {class-name} esm_exchange_grids property."""
        raise TypeError("Cannot delete {class-name} esm_exchange_grids property.")

    def append_to_esm_exchange_grids(self, item):
        """Appends an item to the managed {class-name} esm_exchange_grids collection."""
        if not isinstance(item, GridMosaic):
            raise TypeError("item is of incorrect type.")
        self.__esm_exchange_grids.append(item)

    def remove_from_esm_exchange_grids(self, item):
        """Removes an item from the managed {class-name} esm_exchange_grids collection."""
        if not isinstance(item, GridMosaic):
            raise TypeError("item is of incorrect type.")
        self.__esm_exchange_grids.remove(item)


    @property
    def esm_model_grids(self):
        """Gets value of {class-name} esm_model_grids property."""
        return list(self.__esm_model_grids)

    @esm_model_grids.setter
    def esm_model_grids(self, value):
        """Sets value of {class-name} esm_model_grids property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__esm_model_grids = []
        for i in value:
            self.append_to_esm_model_grids(i)

    @esm_model_grids.deleter
    def esm_model_grids(self, value):
        """Deletes {class-name} esm_model_grids property."""
        raise TypeError("Cannot delete {class-name} esm_model_grids property.")

    def append_to_esm_model_grids(self, item):
        """Appends an item to the managed {class-name} esm_model_grids collection."""
        if not isinstance(item, GridMosaic):
            raise TypeError("item is of incorrect type.")
        self.__esm_model_grids.append(item)

    def remove_from_esm_model_grids(self, item):
        """Removes an item from the managed {class-name} esm_model_grids collection."""
        if not isinstance(item, GridMosaic):
            raise TypeError("item is of incorrect type.")
        self.__esm_model_grids.remove(item)



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
        append(d, 'cim_info', self.__cim_info, False, False, False)
        append(d, 'esm_exchange_grids', self.__esm_exchange_grids, True, False, False)
        append(d, 'esm_model_grids', self.__esm_model_grids, True, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridSpec()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridSpec', e)
