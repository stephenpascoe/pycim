"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-20 16:28:50.016191.
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
from pycim.v1_5.types.activity.activity import Activity



# Module exports.
__all__ = ['NumericalActivity']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-20 16:28:50.016191$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class NumericalActivity(Activity):
    """An abstract class within the cim v1.5 type system.

    
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(NumericalActivity, self).__init__()

        self.__description = str()                                  # type = str
        self.__long_name = str()                                    # type = str
        self.__short_name = str()                                   # type = str


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of the experiment."""
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

        The name of the experiment (that is recognized externally)."""
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
        """Gets value of numerical activity short_name property.

        The name of the experiment (that is used internally)."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of numerical activity short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes numerical activity short_name property."""
        raise TypeError("Cannot delete numerical activity short_name property.")



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
        d = dict(super(NumericalActivity, self).as_dict())
        append(d, 'description', self.__description, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        return d






# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.


