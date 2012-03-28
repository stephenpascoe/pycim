"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.697481.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.activity.simulation import Simulation
from pycim.v1_5.types.shared.cim_info import CimInfo
from pycim.v1_5.types.shared.date_range import DateRange
from pycim.v1_5.types.software.model_component import ModelComponent
from pycim.v1_5.types.shared.cim_reference import CimReference



# Module exports.
__all__ = ['SimulationRun']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.697481$"
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
        self.__date_range = None                                    # type = shared.DateRange
        self.__model = None                                         # type = software.ModelComponent
        self.__model_reference = None                               # type = shared.CimReference


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


    @property
    def date_range(self):
        """Gets value of simulation run date_range property."""
        return self.__date_range

    @date_range.setter
    def date_range(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, DateRange):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation run date_range property."""
        self.__date_range = value

    @date_range.deleter
    def date_range(self, value):
        """Deletes simulation run date_range property."""
        raise TypeError("Cannot delete simulation run date_range property.")


    @property
    def model(self):
        """Gets value of {class-name} model property."""
        return self.__model

    @model.setter
    def model(self, value):
        if value is not None and not isinstance(value, ModelComponent):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} model property."""
        self.__model = value

    @model.deleter
    def model(self, value):
        """Deletes {class-name} model property."""
        raise TypeError("Cannot delete {class-name} model property.")


    @property
    def model_reference(self):
        """Gets value of {class-name} model_reference property."""
        return self.__model_reference

    @model_reference.setter
    def model_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} model_reference property."""
        self.__model_reference = value

    @model_reference.deleter
    def model_reference(self, value):
        """Deletes {class-name} model_reference property."""
        raise TypeError("Cannot delete {class-name} model_reference property.")



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
        append(d, 'date_range', self.__date_range, False, False, False)
        append(d, 'model', self.__model, False, False, False)
        append(d, 'model_reference', self.__model_reference, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = SimulationRun()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.SimulationRun', e)
