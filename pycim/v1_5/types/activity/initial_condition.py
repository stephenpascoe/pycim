"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-20 16:28:50.014699.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.activity.numerical_requirement import NumericalRequirement



# Module exports.
__all__ = ['InitialCondition']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-20 16:28:50.014699$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class InitialCondition(NumericalRequirement):
    """A class within the cim v1.5 type system.

    An initial condition is a numerical requirement on a model prognostic variable value at time zero.
    """
    def __init__(self):
        """Constructor"""
        super(InitialCondition, self).__init__()

        pass


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
        d = dict(super(InitialCondition, self).as_dict())
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = InitialCondition()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.InitialCondition', e)