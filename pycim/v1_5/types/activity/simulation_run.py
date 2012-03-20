"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-20 16:28:50.026253.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.activity.simulation import Simulation
from pycim.v1_5.types.shared.cim_info import CimInfo



# Module exports.
__all__ = ['SimulationRun']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-20 16:28:50.026253$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SimulationRun(Simulation):
    """A class within the cim v1.5 type system.

    A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.
    """
    def __init__(self):
        """Constructor"""
        super(SimulationRun, self).__init__()

        self.__cim_info = None                                      # type = shared.CimInfo


    @property
    def cim_info(self):
        """Gets value of simulation run cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation run cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes simulation run cim_info property."""
        raise TypeError("Cannot delete simulation run cim_info property.")



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
        d = dict(super(SimulationRun, self).as_dict())
        append(d, 'cim_info', self.__cim_info, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = SimulationRun()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.SimulationRun', e)
