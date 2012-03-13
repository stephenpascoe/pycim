"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-13 14:59:06.905125.
"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.date_range import DateRange



# Module exports.
__all__ = ['Calendar']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-13 14:59:06.905125$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Calendar(object):
    """An abstract class within the cim v1.5 type system.

    Describes a method of calculating a span of dates.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Calendar, self).__init__()

        self.__description = str()                                  # type = str
        self.__length = int()                                       # type = int
        self.__range = None                                         # type = shared.DateRange


    @property
    def description(self):
        """Gets value of {class-name} description property.

        Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)"""
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
    def length(self):
        """Gets value of {class-name} length property."""
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
    def range(self):
        """Gets value of {class-name} range property."""
        return self.__range

    @range.setter
    def range(self, value):
        if value is not None and not isinstance(value, DateRange):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} range property."""
        self.__range = value

    @range.deleter
    def range(self, value):
        """Deletes {class-name} range property."""
        raise TypeError("Cannot delete {class-name} range property.")



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
        append(d, 'length', self.__length, False, True, False)
        append(d, 'range', self.__range, False, False, False)
        return d






# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.


