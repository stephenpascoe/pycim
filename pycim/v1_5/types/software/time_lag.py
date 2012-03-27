"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-27 17:29:37.111765.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.software.timing_units import TimingUnits



# Module exports.
__all__ = ['TimeLag']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-27 17:29:37.111765$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class TimeLag(object):
    """A class within the cim v1.5 type system.

    The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.
    """
    def __init__(self):
        """Constructor"""
        super(TimeLag, self).__init__()

        self.__units = None                                         # type = software.TimingUnits
        self.__value = int()                                        # type = int


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


    @property
    def value(self):
        """Gets value of {class-name} value property."""
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} value property."""
        self.__value = value

    @value.deleter
    def value(self, value):
        """Deletes {class-name} value property."""
        raise TypeError("Cannot delete {class-name} value property.")



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
        append(d, 'units', self.__units, False, False, True)
        append(d, 'value', self.__value, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = TimeLag()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.TimeLag', e)
