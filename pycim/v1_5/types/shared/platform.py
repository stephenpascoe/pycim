"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.762563.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.cim_info import CimInfo
from pycim.v1_5.types.shared.responsible_party import ResponsibleParty
from pycim.v1_5.types.shared.machine_compiler_unit import MachineCompilerUnit



# Module exports.
__all__ = ['Platform']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.762563$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Platform(object):
    """A class within the cim v1.5 type system.

    A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.
    """
    def __init__(self):
        """Constructor"""
        super(Platform, self).__init__()

        self.__cim_info = None                                      # type = shared.CimInfo
        self.__contacts = []                                        # type = shared.ResponsibleParty
        self.__description = str()                                  # type = str
        self.__long_name = str()                                    # type = str
        self.__short_name = str()                                   # type = str
        self.__units = []                                           # type = shared.MachineCompilerUnit


    @property
    def cim_info(self):
        """Gets value of platform cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of platform cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes platform cim_info property."""
        raise TypeError("Cannot delete platform cim_info property.")


    @property
    def contacts(self):
        """Gets value of {class-name} contacts property."""
        return list(self.__contacts)

    @contacts.setter
    def contacts(self, value):
        """Sets value of {class-name} contacts property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__contacts = []
        for i in value:
            self.append_to_contacts(i)

    @contacts.deleter
    def contacts(self, value):
        """Deletes {class-name} contacts property."""
        raise TypeError("Cannot delete {class-name} contacts property.")

    def append_to_contacts(self, item):
        """Appends an item to the managed {class-name} contacts collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__contacts.append(item)

    def remove_from_contacts(self, item):
        """Removes an item from the managed {class-name} contacts collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__contacts.remove(item)


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
    def long_name(self):
        """Gets value of {class-name} long_name property."""
        return self.__long_name

    @long_name.setter
    def long_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} long_name property."""
        self.__long_name = value

    @long_name.deleter
    def long_name(self, value):
        """Deletes {class-name} long_name property."""
        raise TypeError("Cannot delete {class-name} long_name property.")


    @property
    def short_name(self):
        """Gets value of platform short_name property."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of platform short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes platform short_name property."""
        raise TypeError("Cannot delete platform short_name property.")


    @property
    def units(self):
        """Gets value of {class-name} units property."""
        return list(self.__units)

    @units.setter
    def units(self, value):
        """Sets value of {class-name} units property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__units = []
        for i in value:
            self.append_to_units(i)

    @units.deleter
    def units(self, value):
        """Deletes {class-name} units property."""
        raise TypeError("Cannot delete {class-name} units property.")

    def append_to_units(self, item):
        """Appends an item to the managed {class-name} units collection."""
        if not isinstance(item, MachineCompilerUnit):
            raise TypeError("item is of incorrect type.")
        self.__units.append(item)

    def remove_from_units(self, item):
        """Removes an item from the managed {class-name} units collection."""
        if not isinstance(item, MachineCompilerUnit):
            raise TypeError("item is of incorrect type.")
        self.__units.remove(item)



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
        append(d, 'cim_info', self.__cim_info, False, False, False)
        append(d, 'contacts', self.__contacts, True, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        append(d, 'units', self.__units, True, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = Platform()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.Platform', e)
