"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-13 14:59:06.914497.
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
from pycim.v1_5.types.shared.cim_relationship_direction_type import CimRelationshipDirectionType



# Module exports.
__all__ = ['CimRelationship']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-13 14:59:06.914497$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimRelationship(object):
    """An abstract class within the cim v1.5 type system.

    A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(CimRelationship, self).__init__()

        self.__description = str()                                  # type = str
        self.__direction = None                                     # type = shared.CimRelationshipDirectionType


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
    def direction(self):
        """Gets value of cim relationship direction property."""
        return self.__direction

    @direction.setter
    def direction(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim relationship direction property."""
        self.__direction = value

    @direction.deleter
    def direction(self, value):
        """Deletes cim relationship direction property."""
        raise TypeError("Cannot delete cim relationship direction property.")



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
        append(d, 'direction', self.__direction, False, False, True)
        return d






# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.


