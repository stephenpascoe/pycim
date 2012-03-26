"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-26 18:08:48.793855.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.date_range import DateRange



# Module exports.
__all__ = ['OpenDateRange']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-26 18:08:48.793855$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class OpenDateRange(DateRange):
    """A class within the cim v1.5 type system.

    A date range without a specified start and/or end point.
    """
    def __init__(self):
        """Constructor"""
        super(OpenDateRange, self).__init__()

        self.__end = datetime.datetime.now()                        # type = datetime.datetime
        self.__start = datetime.datetime.now()                      # type = datetime.datetime


    @property
    def end(self):
        """Gets value of {class-name} end property."""
        return self.__end

    @end.setter
    def end(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} end property."""
        self.__end = value

    @end.deleter
    def end(self, value):
        """Deletes {class-name} end property."""
        raise TypeError("Cannot delete {class-name} end property.")


    @property
    def start(self):
        """Gets value of {class-name} start property."""
        return self.__start

    @start.setter
    def start(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} start property."""
        self.__start = value

    @start.deleter
    def start(self, value):
        """Deletes {class-name} start property."""
        raise TypeError("Cannot delete {class-name} start property.")



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
        d = dict(super(OpenDateRange, self).as_dict())
        append(d, 'end', self.__end, False, True, False)
        append(d, 'start', self.__start, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = OpenDateRange()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.OpenDateRange', e)
