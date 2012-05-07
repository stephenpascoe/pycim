"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.293274.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.data_source import DataSource
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.software.connection_property import ConnectionProperty
from pycim.v1_5.types.software.connection_endpoint import ConnectionEndpoint
from pycim.v1_5.types.software.spatial_regridding import SpatialRegridding
from pycim.v1_5.types.software.timing import Timing
from pycim.v1_5.types.software.time_transformation import TimeTransformation
from pycim.v1_5.types.software.processor_component import ProcessorComponent
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.software.connection_type import ConnectionType



# Module exports.
__all__ = ['Connection']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.293274$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Connection(object):
    """A class within the cim v1.5 type system.

    A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.
    """
    def __init__(self):
        """Constructor"""
        super(Connection, self).__init__()

        self.__description = str()                                  # type = str
        self.__priming = None                                       # type = shared.DataSource
        self.__priming_reference = None                             # type = shared.CimReference
        self.__properties = []                                      # type = software.ConnectionProperty
        self.__sources = []                                         # type = software.ConnectionEndpoint
        self.__spatial_regridding = []                              # type = software.SpatialRegridding
        self.__target = None                                        # type = software.ConnectionEndpoint
        self.__time_lag = str()                                     # type = str
        self.__time_profile = None                                  # type = software.Timing
        self.__time_transformation = None                           # type = software.TimeTransformation
        self.__transformers = []                                    # type = software.ProcessorComponent
        self.__transformers_references = []                         # type = shared.CimReference
        self.__type = None                                          # type = software.ConnectionType


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
    def priming(self):
        """Gets value of {class-name} priming property.

        A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created."""
        return self.__priming

    @priming.setter
    def priming(self, value):
        if value is not None and not isinstance(value, DataSource):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} priming property."""
        self.__priming = value

    @priming.deleter
    def priming(self, value):
        """Deletes {class-name} priming property."""
        raise TypeError("Cannot delete {class-name} priming property.")


    @property
    def priming_reference(self):
        """Gets value of {class-name} priming_reference property."""
        return self.__priming_reference

    @priming_reference.setter
    def priming_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} priming_reference property."""
        self.__priming_reference = value

    @priming_reference.deleter
    def priming_reference(self, value):
        """Deletes {class-name} priming_reference property."""
        raise TypeError("Cannot delete {class-name} priming_reference property.")


    @property
    def properties(self):
        """Gets value of {class-name} properties property."""
        return list(self.__properties)

    @properties.setter
    def properties(self, value):
        """Sets value of {class-name} properties property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__properties = []
        for i in value:
            self.append_to_properties(i)

    @properties.deleter
    def properties(self, value):
        """Deletes {class-name} properties property."""
        raise TypeError("Cannot delete {class-name} properties property.")

    def append_to_properties(self, item):
        """Appends an item to the managed {class-name} properties collection."""
        if not isinstance(item, ConnectionProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.append(item)

    def remove_from_properties(self, item):
        """Removes an item from the managed {class-name} properties collection."""
        if not isinstance(item, ConnectionProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.remove(item)


    @property
    def sources(self):
        """Gets value of {class-name} sources property.

        The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource."""
        return list(self.__sources)

    @sources.setter
    def sources(self, value):
        """Sets value of {class-name} sources property.

        The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource."""
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
        if not isinstance(item, ConnectionEndpoint):
            raise TypeError("item is of incorrect type.")
        self.__sources.append(item)

    def remove_from_sources(self, item):
        """Removes an item from the managed {class-name} sources collection."""
        if not isinstance(item, ConnectionEndpoint):
            raise TypeError("item is of incorrect type.")
        self.__sources.remove(item)


    @property
    def spatial_regridding(self):
        """Gets value of {class-name} spatial_regridding property.

        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)"""
        return list(self.__spatial_regridding)

    @spatial_regridding.setter
    def spatial_regridding(self, value):
        """Sets value of {class-name} spatial_regridding property.

        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)"""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__spatial_regridding = []
        for i in value:
            self.append_to_spatial_regridding(i)

    @spatial_regridding.deleter
    def spatial_regridding(self, value):
        """Deletes {class-name} spatial_regridding property."""
        raise TypeError("Cannot delete {class-name} spatial_regridding property.")

    def append_to_spatial_regridding(self, item):
        """Appends an item to the managed {class-name} spatial_regridding collection."""
        if not isinstance(item, SpatialRegridding):
            raise TypeError("item is of incorrect type.")
        self.__spatial_regridding.append(item)

    def remove_from_spatial_regridding(self, item):
        """Removes an item from the managed {class-name} spatial_regridding collection."""
        if not isinstance(item, SpatialRegridding):
            raise TypeError("item is of incorrect type.")
        self.__spatial_regridding.remove(item)


    @property
    def target(self):
        """Gets value of {class-name} target property.

        The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire."""
        return self.__target

    @target.setter
    def target(self, value):
        if value is not None and not isinstance(value, ConnectionEndpoint):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} target property."""
        self.__target = value

    @target.deleter
    def target(self, value):
        """Deletes {class-name} target property."""
        raise TypeError("Cannot delete {class-name} target property.")


    @property
    def time_lag(self):
        """Gets value of {class-name} time_lag property.

        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time."""
        return self.__time_lag

    @time_lag.setter
    def time_lag(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_lag property."""
        self.__time_lag = value

    @time_lag.deleter
    def time_lag(self, value):
        """Deletes {class-name} time_lag property."""
        raise TypeError("Cannot delete {class-name} time_lag property.")


    @property
    def time_profile(self):
        """Gets value of {class-name} time_profile property.

        All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling."""
        return self.__time_profile

    @time_profile.setter
    def time_profile(self, value):
        if value is not None and not isinstance(value, Timing):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_profile property."""
        self.__time_profile = value

    @time_profile.deleter
    def time_profile(self, value):
        """Deletes {class-name} time_profile property."""
        raise TypeError("Cannot delete {class-name} time_profile property.")


    @property
    def time_transformation(self):
        """Gets value of {class-name} time_transformation property.

        Temporal transformation performed on the coupling field before or after regridding onto the target grid."""
        return self.__time_transformation

    @time_transformation.setter
    def time_transformation(self, value):
        if value is not None and not isinstance(value, TimeTransformation):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_transformation property."""
        self.__time_transformation = value

    @time_transformation.deleter
    def time_transformation(self, value):
        """Deletes {class-name} time_transformation property."""
        raise TypeError("Cannot delete {class-name} time_transformation property.")


    @property
    def transformers(self):
        """Gets value of {class-name} transformers property.

        An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here."""
        return list(self.__transformers)

    @transformers.setter
    def transformers(self, value):
        """Sets value of {class-name} transformers property.

        An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__transformers = []
        for i in value:
            self.append_to_transformers(i)

    @transformers.deleter
    def transformers(self, value):
        """Deletes {class-name} transformers property."""
        raise TypeError("Cannot delete {class-name} transformers property.")

    def append_to_transformers(self, item):
        """Appends an item to the managed {class-name} transformers collection."""
        if not isinstance(item, ProcessorComponent):
            raise TypeError("item is of incorrect type.")
        self.__transformers.append(item)

    def remove_from_transformers(self, item):
        """Removes an item from the managed {class-name} transformers collection."""
        if not isinstance(item, ProcessorComponent):
            raise TypeError("item is of incorrect type.")
        self.__transformers.remove(item)


    @property
    def transformers_references(self):
        """Gets value of {class-name} transformers_references property."""
        return list(self.__transformers_references)

    @transformers_references.setter
    def transformers_references(self, value):
        """Sets value of {class-name} transformers_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__transformers_references = []
        for i in value:
            self.append_to_transformers_references(i)

    @transformers_references.deleter
    def transformers_references(self, value):
        """Deletes {class-name} transformers_references property."""
        raise TypeError("Cannot delete {class-name} transformers_references property.")

    def append_to_transformers_references(self, item):
        """Appends an item to the managed {class-name} transformers_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__transformers_references.append(item)

    def remove_from_transformers_references(self, item):
        """Removes an item from the managed {class-name} transformers_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__transformers_references.remove(item)


    @property
    def type(self):
        """Gets value of {class-name} type property.

        The type of Connection"""
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
        append(d, 'priming', self.__priming, False, False, False)
        append(d, 'priming_reference', self.__priming_reference, False, False, False)
        append(d, 'properties', self.__properties, True, False, False)
        append(d, 'sources', self.__sources, True, False, False)
        append(d, 'spatial_regridding', self.__spatial_regridding, True, False, False)
        append(d, 'target', self.__target, False, False, False)
        append(d, 'time_lag', self.__time_lag, False, True, False)
        append(d, 'time_profile', self.__time_profile, False, False, False)
        append(d, 'time_transformation', self.__time_transformation, False, False, False)
        append(d, 'transformers', self.__transformers, True, False, False)
        append(d, 'transformers_references', self.__transformers_references, True, False, False)
        append(d, 'type', self.__type, False, False, True)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = Connection()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Connection', e)
