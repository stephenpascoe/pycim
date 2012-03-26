"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-26 18:08:48.726981.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.activity.activity import Activity



# Module exports.
__all__ = ['MeasurementCampaign']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-26 18:08:48.726981$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class MeasurementCampaign(Activity):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(MeasurementCampaign, self).__init__()

        self.__duration = int()                                     # type = int


    @property
    def duration(self):
        """Gets value of measurement campaign duration property."""
        return self.__duration

    @duration.setter
    def duration(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of measurement campaign duration property."""
        self.__duration = value

    @duration.deleter
    def duration(self, value):
        """Deletes measurement campaign duration property."""
        raise TypeError("Cannot delete measurement campaign duration property.")



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
        d = dict(super(MeasurementCampaign, self).as_dict())
        append(d, 'duration', self.__duration, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = MeasurementCampaign()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.MeasurementCampaign', e)
