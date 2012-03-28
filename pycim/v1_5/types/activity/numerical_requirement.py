"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.685131.
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



# Module exports.
__all__ = ['NumericalRequirement']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.685131$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class NumericalRequirement(object):
    """An abstract class within the cim v1.5 type system.

    A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(NumericalRequirement, self).__init__()

        self.__description = str()                                  # type = str
        self.__id = str()                                           # type = str
        self.__name = str()                                         # type = str
        self.__options = []                                         # type = activity.RequirementOption


    @property
    def description(self):
        """Gets value of {class-name} description property."""
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
    def id(self):
        """Gets value of {class-name} id property."""
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} id property."""
        self.__id = value

    @id.deleter
    def id(self, value):
        """Deletes {class-name} id property."""
        raise TypeError("Cannot delete {class-name} id property.")


    @property
    def name(self):
        """Gets value of numerical requirement name property."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of numerical requirement name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes numerical requirement name property."""
        raise TypeError("Cannot delete numerical requirement name property.")


    @property
    def options(self):
        """Gets value of {class-name} options property."""
        return list(self.__options)

    @options.setter
    def options(self, value):
        """Sets value of {class-name} options property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__options = []
        for i in value:
            self.append_to_options(i)

    @options.deleter
    def options(self, value):
        """Deletes {class-name} options property."""
        raise TypeError("Cannot delete {class-name} options property.")

    def append_to_options(self, item):
        """Appends an item to the managed {class-name} options collection."""
        if not isinstance(item, RequirementOption):
            raise TypeError("item is of incorrect type.")
        self.__options.append(item)

    def remove_from_options(self, item):
        """Removes an item from the managed {class-name} options collection."""
        if not isinstance(item, RequirementOption):
            raise TypeError("item is of incorrect type.")
        self.__options.remove(item)



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
        append(d, 'id', self.__id, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        append(d, 'options', self.__options, True, False, False)
        return d






# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.
from pycim.v1_5.types.activity.requirement_option import RequirementOption


