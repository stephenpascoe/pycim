"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.210720.
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



# Module exports.
__all__ = ['SimulationComposite']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.210720$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SimulationComposite(Simulation):
    """A class within the cim v1.5 type system.

    A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.
    """
    def __init__(self):
        """Constructor"""
        super(SimulationComposite, self).__init__()

        self.__child = []                                           # type = activity.Simulation
        self.__cim_info = None                                      # type = shared.CimInfo
        self.__date_range = None                                    # type = shared.DateRange
        self.__rank = int()                                         # type = int


    @property
    def child(self):
        """Gets value of {class-name} child property."""
        return list(self.__child)

    @child.setter
    def child(self, value):
        """Sets value of {class-name} child property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__child = []
        for i in value:
            self.append_to_child(i)

    @child.deleter
    def child(self, value):
        """Deletes {class-name} child property."""
        raise TypeError("Cannot delete {class-name} child property.")

    def append_to_child(self, item):
        """Appends an item to the managed {class-name} child collection."""
        if not isinstance(item, Simulation):
            raise TypeError("item is of incorrect type.")
        self.__child.append(item)

    def remove_from_child(self, item):
        """Removes an item from the managed {class-name} child collection."""
        if not isinstance(item, Simulation):
            raise TypeError("item is of incorrect type.")
        self.__child.remove(item)


    @property
    def cim_info(self):
        """Gets value of simulation composite cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        #!REVIEW: Only use docstrings at the top of functions/methods.
        #         Use comments in this context.
        """Sets value of simulation composite cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes simulation composite cim_info property."""
        raise TypeError("Cannot delete simulation composite cim_info property.")


    @property
    def date_range(self):
        """Gets value of simulation composite date_range property."""
        return self.__date_range

    @date_range.setter
    def date_range(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, DateRange):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation composite date_range property."""
        self.__date_range = value

    @date_range.deleter
    def date_range(self, value):
        """Deletes simulation composite date_range property."""
        raise TypeError("Cannot delete simulation composite date_range property.")


    @property
    def rank(self):
        """Gets value of simulation composite rank property.

        Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation"""
        return self.__rank

    @rank.setter
    def rank(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation composite rank property."""
        self.__rank = value

    @rank.deleter
    def rank(self, value):
        """Deletes simulation composite rank property."""
        raise TypeError("Cannot delete simulation composite rank property.")



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
        d = dict(super(SimulationComposite, self).as_dict())
        append(d, 'child', self.__child, True, False, False)
        append(d, 'cim_info', self.__cim_info, False, False, False)
        append(d, 'date_range', self.__date_range, False, False, False)
        append(d, 'rank', self.__rank, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = SimulationComposite()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.SimulationComposite', e)
