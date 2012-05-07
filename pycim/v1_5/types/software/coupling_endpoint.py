"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.301804.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.data_source import DataSource
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.software.coupling_property import CouplingProperty



# Module exports.
__all__ = ['CouplingEndpoint']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.301804$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CouplingEndpoint(object):
    """A class within the cim v1.5 type system.

    The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).
    """
    def __init__(self):
        """Constructor"""
        super(CouplingEndpoint, self).__init__()

        self.__data_source = None                                   # type = shared.DataSource
        self.__data_source_reference = None                         # type = shared.CimReference
        self.__instance_id = str()                                  # type = str
        self.__properties = []                                      # type = software.CouplingProperty


    @property
    def data_source(self):
        """Gets value of {class-name} data_source property."""
        return self.__data_source

    @data_source.setter
    def data_source(self, value):
        if value is not None and not isinstance(value, DataSource):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} data_source property."""
        self.__data_source = value

    @data_source.deleter
    def data_source(self, value):
        """Deletes {class-name} data_source property."""
        raise TypeError("Cannot delete {class-name} data_source property.")


    @property
    def data_source_reference(self):
        """Gets value of {class-name} data_source_reference property."""
        return self.__data_source_reference

    @data_source_reference.setter
    def data_source_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} data_source_reference property."""
        self.__data_source_reference = value

    @data_source_reference.deleter
    def data_source_reference(self, value):
        """Deletes {class-name} data_source_reference property."""
        raise TypeError("Cannot delete {class-name} data_source_reference property.")


    @property
    def instance_id(self):
        """Gets value of {class-name} instance_id property.

        If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG)."""
        return self.__instance_id

    @instance_id.setter
    def instance_id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} instance_id property."""
        self.__instance_id = value

    @instance_id.deleter
    def instance_id(self, value):
        """Deletes {class-name} instance_id property."""
        raise TypeError("Cannot delete {class-name} instance_id property.")


    @property
    def properties(self):
        """Gets value of {class-name} properties property.

        A place to describe features specific to the source/target of a coupling"""
        return list(self.__properties)

    @properties.setter
    def properties(self, value):
        """Sets value of {class-name} properties property.

        A place to describe features specific to the source/target of a coupling"""
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
        if not isinstance(item, CouplingProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.append(item)

    def remove_from_properties(self, item):
        """Removes an item from the managed {class-name} properties collection."""
        if not isinstance(item, CouplingProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.remove(item)



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
        append(d, 'data_source', self.__data_source, False, False, False)
        append(d, 'data_source_reference', self.__data_source_reference, False, False, False)
        append(d, 'instance_id', self.__instance_id, False, True, False)
        append(d, 'properties', self.__properties, True, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = CouplingEndpoint()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.CouplingEndpoint', e)
