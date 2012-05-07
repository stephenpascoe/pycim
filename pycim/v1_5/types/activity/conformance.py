"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.188292.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.activity.frequency_type import FrequencyType
from pycim.v1_5.types.activity.numerical_requirement import NumericalRequirement
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.shared.data_source import DataSource
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.activity.conformance_type import ConformanceType



# Module exports.
__all__ = ['Conformance']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.188292$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Conformance(object):
    """A class within the cim v1.5 type system.

    A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.
    """
    def __init__(self):
        """Constructor"""
        super(Conformance, self).__init__()

        self.__description = str()                                  # type = str
        self.__frequency = None                                     # type = activity.FrequencyType
        self.__is_conformant = bool()                               # type = bool
        self.__requirements = []                                    # type = activity.NumericalRequirement
        self.__requirements_references = []                         # type = shared.CimReference
        self.__sources = []                                         # type = shared.DataSource
        self.__sources_references = []                              # type = shared.CimReference
        self.__type = None                                          # type = activity.ConformanceType


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
    def frequency(self):
        """Gets value of {class-name} frequency property."""
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} frequency property."""
        self.__frequency = value

    @frequency.deleter
    def frequency(self, value):
        """Deletes {class-name} frequency property."""
        raise TypeError("Cannot delete {class-name} frequency property.")


    @property
    def is_conformant(self):
        """Gets value of conformance is_conformant property.

        Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false."""
        return self.__is_conformant

    @is_conformant.setter
    def is_conformant(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, bool):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of conformance is_conformant property."""
        self.__is_conformant = value

    @is_conformant.deleter
    def is_conformant(self, value):
        """Deletes conformance is_conformant property."""
        raise TypeError("Cannot delete conformance is_conformant property.")


    @property
    def requirements(self):
        """Gets value of {class-name} requirements property.

        Points to the NumericalRequirement that the simulation in question is conforming to."""
        return list(self.__requirements)

    @requirements.setter
    def requirements(self, value):
        """Sets value of {class-name} requirements property.

        Points to the NumericalRequirement that the simulation in question is conforming to."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__requirements = []
        for i in value:
            self.append_to_requirements(i)

    @requirements.deleter
    def requirements(self, value):
        """Deletes {class-name} requirements property."""
        raise TypeError("Cannot delete {class-name} requirements property.")

    def append_to_requirements(self, item):
        """Appends an item to the managed {class-name} requirements collection."""
        if not isinstance(item, NumericalRequirement):
            raise TypeError("item is of incorrect type.")
        self.__requirements.append(item)

    def remove_from_requirements(self, item):
        """Removes an item from the managed {class-name} requirements collection."""
        if not isinstance(item, NumericalRequirement):
            raise TypeError("item is of incorrect type.")
        self.__requirements.remove(item)


    @property
    def requirements_references(self):
        """Gets value of {class-name} requirements_references property."""
        return list(self.__requirements_references)

    @requirements_references.setter
    def requirements_references(self, value):
        """Sets value of {class-name} requirements_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__requirements_references = []
        for i in value:
            self.append_to_requirements_references(i)

    @requirements_references.deleter
    def requirements_references(self, value):
        """Deletes {class-name} requirements_references property."""
        raise TypeError("Cannot delete {class-name} requirements_references property.")

    def append_to_requirements_references(self, item):
        """Appends an item to the managed {class-name} requirements_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__requirements_references.append(item)

    def remove_from_requirements_references(self, item):
        """Removes an item from the managed {class-name} requirements_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__requirements_references.remove(item)


    @property
    def sources(self):
        """Gets value of {class-name} sources property.

        Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute."""
        return list(self.__sources)

    @sources.setter
    def sources(self, value):
        """Sets value of {class-name} sources property.

        Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__sources = []
        for i in value:
            self.append_to_sources(i)

    @sources.deleter
    def sources(self, value):
        """Deletes {class-name} sources property."""
        raise TypeError("Cannot delete {class-name} sources property.")

    def append_to_sources(self, item):
        """Appends an item to the managed {class-name} sources collection."""
        if not isinstance(item, DataSource):
            raise TypeError("item is of incorrect type.")
        self.__sources.append(item)

    def remove_from_sources(self, item):
        """Removes an item from the managed {class-name} sources collection."""
        if not isinstance(item, DataSource):
            raise TypeError("item is of incorrect type.")
        self.__sources.remove(item)


    @property
    def sources_references(self):
        """Gets value of {class-name} sources_references property."""
        return list(self.__sources_references)

    @sources_references.setter
    def sources_references(self, value):
        """Sets value of {class-name} sources_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__sources_references = []
        for i in value:
            self.append_to_sources_references(i)

    @sources_references.deleter
    def sources_references(self, value):
        """Deletes {class-name} sources_references property."""
        raise TypeError("Cannot delete {class-name} sources_references property.")

    def append_to_sources_references(self, item):
        """Appends an item to the managed {class-name} sources_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__sources_references.append(item)

    def remove_from_sources_references(self, item):
        """Removes an item from the managed {class-name} sources_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__sources_references.remove(item)


    @property
    def type(self):
        """Gets value of {class-name} type property.

        Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)"""
        return self.__type

    @type.setter
    def type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes {class-name} type property."""
        raise TypeError("Cannot delete {class-name} type property.")



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
        append(d, 'frequency', self.__frequency, False, False, True)
        append(d, 'is_conformant', self.__is_conformant, False, True, False)
        append(d, 'requirements', self.__requirements, True, False, False)
        append(d, 'requirements_references', self.__requirements_references, True, False, False)
        append(d, 'sources', self.__sources, True, False, False)
        append(d, 'sources_references', self.__sources_references, True, False, False)
        append(d, 'type', self.__type, False, False, True)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = Conformance()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.Conformance', e)
