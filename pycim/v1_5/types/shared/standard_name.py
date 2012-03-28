"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.770405.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.standard import Standard



# Module exports.
__all__ = ['StandardName']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.770405$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class StandardName(object):
    """A class within the cim v1.5 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.
    """
    def __init__(self):
        """Constructor"""
        super(StandardName, self).__init__()

        self.__is_open = bool()                                     # type = bool
        self.__standards = []                                       # type = shared.Standard
        self.__value = str()                                        # type = str


    @property
    def is_open(self):
        """Gets value of standard name is_open property."""
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, bool):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of standard name is_open property."""
        self.__is_open = value

    @is_open.deleter
    def is_open(self, value):
        """Deletes standard name is_open property."""
        raise TypeError("Cannot delete standard name is_open property.")


    @property
    def standards(self):
        """Gets value of {class-name} standards property.

        Details of the standard being used."""
        return list(self.__standards)

    @standards.setter
    def standards(self, value):
        """Sets value of {class-name} standards property.

        Details of the standard being used."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__standards = []
        for i in value:
            self.append_to_standards(i)

    @standards.deleter
    def standards(self, value):
        """Deletes {class-name} standards property."""
        raise TypeError("Cannot delete {class-name} standards property.")

    def append_to_standards(self, item):
        """Appends an item to the managed {class-name} standards collection."""
        if not isinstance(item, Standard):
            raise TypeError("item is of incorrect type.")
        self.__standards.append(item)

    def remove_from_standards(self, item):
        """Removes an item from the managed {class-name} standards collection."""
        if not isinstance(item, Standard):
            raise TypeError("item is of incorrect type.")
        self.__standards.remove(item)


    @property
    def value(self):
        """Gets value of standard name value property."""
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of standard name value property."""
        self.__value = value

    @value.deleter
    def value(self, value):
        """Deletes standard name value property."""
        raise TypeError("Cannot delete standard name value property.")



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
        append(d, 'is_open', self.__is_open, False, True, False)
        append(d, 'standards', self.__standards, True, False, False)
        append(d, 'value', self.__value, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = StandardName()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.StandardName', e)
