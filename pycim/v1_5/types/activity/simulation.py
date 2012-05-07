"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.207784.
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
from pycim.v1_5.types.activity.numerical_activity import NumericalActivity
from pycim.v1_5.types.shared.calendar import Calendar
from pycim.v1_5.types.activity.conformance import Conformance
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.software.deployment import Deployment
from pycim.v1_5.types.software.coupling import Coupling
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.data.data_object import DataObject
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.data.data_object import DataObject
from pycim.v1_5.types.shared.closed_date_range import ClosedDateRange
from pycim.v1_5.types.shared.cim_reference import CimReference



# Module exports.
__all__ = ['Simulation']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.207784$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Simulation(NumericalActivity):
    """An abstract class within the cim v1.5 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Simulation, self).__init__()

        self.__authors = str()                                      # type = str
        self.__calendar = None                                      # type = shared.Calendar
        self.__conformances = []                                    # type = activity.Conformance
        self.__control_simulation = None                            # type = activity.Simulation
        self.__control_simulation_reference = None                  # type = shared.CimReference
        self.__deployments = []                                     # type = software.Deployment
        self.__inputs = []                                          # type = software.Coupling
        self.__output_references = []                               # type = shared.CimReference
        self.__outputs = []                                         # type = data.DataObject
        self.__restart_references = []                              # type = shared.CimReference
        self.__restarts = []                                        # type = data.DataObject
        self.__simulation_id = str()                                # type = str
        self.__spinup_date_range = None                             # type = shared.ClosedDateRange
        self.__spinup_simulation = None                             # type = activity.Simulation
        self.__spinup_simulation_reference = None                   # type = shared.CimReference


    @property
    def authors(self):
        """Gets value of {class-name} authors property.

        List of associated authors."""
        return self.__authors

    @authors.setter
    def authors(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} authors property."""
        self.__authors = value

    @authors.deleter
    def authors(self, value):
        """Deletes {class-name} authors property."""
        raise TypeError("Cannot delete {class-name} authors property.")


    @property
    def calendar(self):
        """Gets value of simulation calendar property."""
        return self.__calendar

    @calendar.setter
    def calendar(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, Calendar):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation calendar property."""
        self.__calendar = value

    @calendar.deleter
    def calendar(self, value):
        """Deletes simulation calendar property."""
        raise TypeError("Cannot delete simulation calendar property.")


    @property
    def conformances(self):
        """Gets value of {class-name} conformances property."""
        return list(self.__conformances)

    @conformances.setter
    def conformances(self, value):
        """Sets value of {class-name} conformances property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__conformances = []
        for i in value:
            self.append_to_conformances(i)

    @conformances.deleter
    def conformances(self, value):
        """Deletes {class-name} conformances property."""
        raise TypeError("Cannot delete {class-name} conformances property.")

    def append_to_conformances(self, item):
        """Appends an item to the managed {class-name} conformances collection."""
        if not isinstance(item, Conformance):
            raise TypeError("item is of incorrect type.")
        self.__conformances.append(item)

    def remove_from_conformances(self, item):
        """Removes an item from the managed {class-name} conformances collection."""
        if not isinstance(item, Conformance):
            raise TypeError("item is of incorrect type.")
        self.__conformances.remove(item)


    @property
    def control_simulation(self):
        """Gets value of {class-name} control_simulation property.

        Points to a simulation being used as the basis (control) run.  Note that only "derived" simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run."""
        return self.__control_simulation

    @control_simulation.setter
    def control_simulation(self, value):
        if value is not None and not isinstance(value, Simulation):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} control_simulation property."""
        self.__control_simulation = value

    @control_simulation.deleter
    def control_simulation(self, value):
        """Deletes {class-name} control_simulation property."""
        raise TypeError("Cannot delete {class-name} control_simulation property.")


    @property
    def control_simulation_reference(self):
        """Gets value of {class-name} control_simulation_reference property."""
        return self.__control_simulation_reference

    @control_simulation_reference.setter
    def control_simulation_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} control_simulation_reference property."""
        self.__control_simulation_reference = value

    @control_simulation_reference.deleter
    def control_simulation_reference(self, value):
        """Deletes {class-name} control_simulation_reference property."""
        raise TypeError("Cannot delete {class-name} control_simulation_reference property.")


    @property
    def deployments(self):
        """Gets value of {class-name} deployments property."""
        return list(self.__deployments)

    @deployments.setter
    def deployments(self, value):
        """Sets value of {class-name} deployments property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__deployments = []
        for i in value:
            self.append_to_deployments(i)

    @deployments.deleter
    def deployments(self, value):
        """Deletes {class-name} deployments property."""
        raise TypeError("Cannot delete {class-name} deployments property.")

    def append_to_deployments(self, item):
        """Appends an item to the managed {class-name} deployments collection."""
        if not isinstance(item, Deployment):
            raise TypeError("item is of incorrect type.")
        self.__deployments.append(item)

    def remove_from_deployments(self, item):
        """Removes an item from the managed {class-name} deployments collection."""
        if not isinstance(item, Deployment):
            raise TypeError("item is of incorrect type.")
        self.__deployments.remove(item)


    @property
    def inputs(self):
        """Gets value of {class-name} inputs property.

        Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc."""
        return list(self.__inputs)

    @inputs.setter
    def inputs(self, value):
        """Sets value of {class-name} inputs property.

        Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__inputs = []
        for i in value:
            self.append_to_inputs(i)

    @inputs.deleter
    def inputs(self, value):
        """Deletes {class-name} inputs property."""
        raise TypeError("Cannot delete {class-name} inputs property.")

    def append_to_inputs(self, item):
        """Appends an item to the managed {class-name} inputs collection."""
        if not isinstance(item, Coupling):
            raise TypeError("item is of incorrect type.")
        self.__inputs.append(item)

    def remove_from_inputs(self, item):
        """Removes an item from the managed {class-name} inputs collection."""
        if not isinstance(item, Coupling):
            raise TypeError("item is of incorrect type.")
        self.__inputs.remove(item)


    @property
    def output_references(self):
        """Gets value of {class-name} output_references property."""
        return list(self.__output_references)

    @output_references.setter
    def output_references(self, value):
        """Sets value of {class-name} output_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__output_references = []
        for i in value:
            self.append_to_output_references(i)

    @output_references.deleter
    def output_references(self, value):
        """Deletes {class-name} output_references property."""
        raise TypeError("Cannot delete {class-name} output_references property.")

    def append_to_output_references(self, item):
        """Appends an item to the managed {class-name} output_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__output_references.append(item)

    def remove_from_output_references(self, item):
        """Removes an item from the managed {class-name} output_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__output_references.remove(item)


    @property
    def outputs(self):
        """Gets value of {class-name} outputs property."""
        return list(self.__outputs)

    @outputs.setter
    def outputs(self, value):
        """Sets value of {class-name} outputs property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__outputs = []
        for i in value:
            self.append_to_outputs(i)

    @outputs.deleter
    def outputs(self, value):
        """Deletes {class-name} outputs property."""
        raise TypeError("Cannot delete {class-name} outputs property.")

    def append_to_outputs(self, item):
        """Appends an item to the managed {class-name} outputs collection."""
        if not isinstance(item, DataObject):
            raise TypeError("item is of incorrect type.")
        self.__outputs.append(item)

    def remove_from_outputs(self, item):
        """Removes an item from the managed {class-name} outputs collection."""
        if not isinstance(item, DataObject):
            raise TypeError("item is of incorrect type.")
        self.__outputs.remove(item)


    @property
    def restart_references(self):
        """Gets value of {class-name} restart_references property."""
        return list(self.__restart_references)

    @restart_references.setter
    def restart_references(self, value):
        """Sets value of {class-name} restart_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__restart_references = []
        for i in value:
            self.append_to_restart_references(i)

    @restart_references.deleter
    def restart_references(self, value):
        """Deletes {class-name} restart_references property."""
        raise TypeError("Cannot delete {class-name} restart_references property.")

    def append_to_restart_references(self, item):
        """Appends an item to the managed {class-name} restart_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__restart_references.append(item)

    def remove_from_restart_references(self, item):
        """Removes an item from the managed {class-name} restart_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__restart_references.remove(item)


    @property
    def restarts(self):
        """Gets value of {class-name} restarts property."""
        return list(self.__restarts)

    @restarts.setter
    def restarts(self, value):
        """Sets value of {class-name} restarts property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__restarts = []
        for i in value:
            self.append_to_restarts(i)

    @restarts.deleter
    def restarts(self, value):
        """Deletes {class-name} restarts property."""
        raise TypeError("Cannot delete {class-name} restarts property.")

    def append_to_restarts(self, item):
        """Appends an item to the managed {class-name} restarts collection."""
        if not isinstance(item, DataObject):
            raise TypeError("item is of incorrect type.")
        self.__restarts.append(item)

    def remove_from_restarts(self, item):
        """Removes an item from the managed {class-name} restarts collection."""
        if not isinstance(item, DataObject):
            raise TypeError("item is of incorrect type.")
        self.__restarts.remove(item)


    @property
    def simulation_id(self):
        """Gets value of {class-name} simulation_id property."""
        return self.__simulation_id

    @simulation_id.setter
    def simulation_id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} simulation_id property."""
        self.__simulation_id = value

    @simulation_id.deleter
    def simulation_id(self, value):
        """Deletes {class-name} simulation_id property."""
        raise TypeError("Cannot delete {class-name} simulation_id property.")


    @property
    def spinup_date_range(self):
        """Gets value of {class-name} spinup_date_range property.

        The date range that a simulation is engaged in spinup."""
        return self.__spinup_date_range

    @spinup_date_range.setter
    def spinup_date_range(self, value):
        if value is not None and not isinstance(value, ClosedDateRange):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} spinup_date_range property."""
        self.__spinup_date_range = value

    @spinup_date_range.deleter
    def spinup_date_range(self, value):
        """Deletes {class-name} spinup_date_range property."""
        raise TypeError("Cannot delete {class-name} spinup_date_range property.")


    @property
    def spinup_simulation(self):
        """Gets value of {class-name} spinup_simulation property.

        The (external) simulation used during "spinup."  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup."""
        return self.__spinup_simulation

    @spinup_simulation.setter
    def spinup_simulation(self, value):
        if value is not None and not isinstance(value, Simulation):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} spinup_simulation property."""
        self.__spinup_simulation = value

    @spinup_simulation.deleter
    def spinup_simulation(self, value):
        """Deletes {class-name} spinup_simulation property."""
        raise TypeError("Cannot delete {class-name} spinup_simulation property.")


    @property
    def spinup_simulation_reference(self):
        """Gets value of {class-name} spinup_simulation_reference property."""
        return self.__spinup_simulation_reference

    @spinup_simulation_reference.setter
    def spinup_simulation_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} spinup_simulation_reference property."""
        self.__spinup_simulation_reference = value

    @spinup_simulation_reference.deleter
    def spinup_simulation_reference(self, value):
        """Deletes {class-name} spinup_simulation_reference property."""
        raise TypeError("Cannot delete {class-name} spinup_simulation_reference property.")



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
        d = dict(super(Simulation, self).as_dict())
        append(d, 'authors', self.__authors, False, True, False)
        append(d, 'calendar', self.__calendar, False, False, False)
        append(d, 'conformances', self.__conformances, True, False, False)
        append(d, 'control_simulation', self.__control_simulation, False, False, False)
        append(d, 'control_simulation_reference', self.__control_simulation_reference, False, False, False)
        append(d, 'deployments', self.__deployments, True, False, False)
        append(d, 'inputs', self.__inputs, True, False, False)
        append(d, 'output_references', self.__output_references, True, False, False)
        append(d, 'outputs', self.__outputs, True, False, False)
        append(d, 'restart_references', self.__restart_references, True, False, False)
        append(d, 'restarts', self.__restarts, True, False, False)
        append(d, 'simulation_id', self.__simulation_id, False, True, False)
        append(d, 'spinup_date_range', self.__spinup_date_range, False, False, False)
        append(d, 'spinup_simulation', self.__spinup_simulation, False, False, False)
        append(d, 'spinup_simulation_reference', self.__spinup_simulation_reference, False, False, False)
        return d






# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.


