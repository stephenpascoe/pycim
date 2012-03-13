"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-13 14:59:06.882373.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.activity.numerical_requirement import NumericalRequirement
from pycim.v1_5.types.shared.date_range import DateRange
from pycim.v1_5.types.activity.resolution_type import ResolutionType



# Module exports.
__all__ = ['SpatioTemporalConstraint']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-13 14:59:06.882373$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SpatioTemporalConstraint(NumericalRequirement):
    """A class within the cim v1.5 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor"""
        super(SpatioTemporalConstraint, self).__init__()

        self.__date_range = None                                    # type = shared.DateRange
        self.__spatial_resolution = None                            # type = activity.ResolutionType


    @property
    def date_range(self):
        """Gets value of {class-name} date_range property."""
        return self.__date_range

    @date_range.setter
    def date_range(self, value):
        if value is not None and not isinstance(value, DateRange):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} date_range property."""
        self.__date_range = value

    @date_range.deleter
    def date_range(self, value):
        """Deletes {class-name} date_range property."""
        raise TypeError("Cannot delete {class-name} date_range property.")


    @property
    def spatial_resolution(self):
        """Gets value of {class-name} spatial_resolution property."""
        return self.__spatial_resolution

    @spatial_resolution.setter
    def spatial_resolution(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} spatial_resolution property."""
        self.__spatial_resolution = value

    @spatial_resolution.deleter
    def spatial_resolution(self, value):
        """Deletes {class-name} spatial_resolution property."""
        raise TypeError("Cannot delete {class-name} spatial_resolution property.")



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
        d = dict(super(SpatioTemporalConstraint, self).as_dict())
        append(d, 'date_range', self.__date_range, False, False, False)
        append(d, 'spatial_resolution', self.__spatial_resolution, False, False, True)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = SpatioTemporalConstraint()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.SpatioTemporalConstraint', e)
