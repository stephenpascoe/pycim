"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.204816.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.



# Module exports.
__all__ = ['RequirementOption']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.204816$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class RequirementOption(object):
    """A class within the cim v1.5 type system.

    A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).
    """
    def __init__(self):
        """Constructor"""
        super(RequirementOption, self).__init__()

        self.__relationship = str()                                 # type = str
        self.__requirement = None                                   # type = activity.NumericalRequirement


    @property
    def relationship(self):
        """Gets value of {class-name} relationship property.

        Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an "OR" relationship meaning use this boundary condition _or_ that one."""
        return self.__relationship

    @relationship.setter
    def relationship(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} relationship property."""
        self.__relationship = value

    @relationship.deleter
    def relationship(self, value):
        """Deletes {class-name} relationship property."""
        raise TypeError("Cannot delete {class-name} relationship property.")


    @property
    def requirement(self):
        """Gets value of {class-name} requirement property.

        The requirement being specified by this option"""
        return self.__requirement

    @requirement.setter
    def requirement(self, value):
        if value is not None and not isinstance(value, NumericalRequirement):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} requirement property."""
        self.__requirement = value

    @requirement.deleter
    def requirement(self, value):
        """Deletes {class-name} requirement property."""
        raise TypeError("Cannot delete {class-name} requirement property.")



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
        append(d, 'relationship', self.__relationship, False, True, False)
        append(d, 'requirement', self.__requirement, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.
from pycim.v1_5.types.activity.numerical_requirement import NumericalRequirement



# Command line entry point.
if __name__ == "__main__":
    try:
        i = RequirementOption()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.RequirementOption', e)
