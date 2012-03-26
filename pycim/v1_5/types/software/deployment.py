"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-26 18:08:48.812570.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.software.parallelisation import Parallelisation
from pycim.v1_5.types.shared.platform import Platform
from pycim.v1_5.types.shared.cim_reference import CimReference



# Module exports.
__all__ = ['Deployment']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-26 18:08:48.812570$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Deployment(object):
    """A class within the cim v1.5 type system.

    Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.
    """
    def __init__(self):
        """Constructor"""
        super(Deployment, self).__init__()

        self.__deployment_date = datetime.datetime.now()            # type = datetime.datetime
        self.__description = str()                                  # type = str
        self.__executable_arguments = []                            # type = str
        self.__executable_name = str()                              # type = str
        self.__parallelisation = None                               # type = software.Parallelisation
        self.__platform = None                                      # type = shared.Platform
        self.__platform_reference = None                            # type = shared.CimReference


    @property
    def deployment_date(self):
        """Gets value of {class-name} deployment_date property."""
        return self.__deployment_date

    @deployment_date.setter
    def deployment_date(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} deployment_date property."""
        self.__deployment_date = value

    @deployment_date.deleter
    def deployment_date(self, value):
        """Deletes {class-name} deployment_date property."""
        raise TypeError("Cannot delete {class-name} deployment_date property.")


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
    def executable_arguments(self):
        """Gets value of {class-name} executable_arguments property."""
        return list(self.__executable_arguments)

    @executable_arguments.setter
    def executable_arguments(self, value):
        """Sets value of {class-name} executable_arguments property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__executable_arguments = []
        for i in value:
            self.append_to_executable_arguments(i)

    @executable_arguments.deleter
    def executable_arguments(self, value):
        """Deletes {class-name} executable_arguments property."""
        raise TypeError("Cannot delete {class-name} executable_arguments property.")

    def append_to_executable_arguments(self, item):
        """Appends an item to the managed {class-name} executable_arguments collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__executable_arguments.append(item)

    def remove_from_executable_arguments(self, item):
        """Removes an item from the managed {class-name} executable_arguments collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__executable_arguments.remove(item)


    @property
    def executable_name(self):
        """Gets value of {class-name} executable_name property."""
        return self.__executable_name

    @executable_name.setter
    def executable_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} executable_name property."""
        self.__executable_name = value

    @executable_name.deleter
    def executable_name(self, value):
        """Deletes {class-name} executable_name property."""
        raise TypeError("Cannot delete {class-name} executable_name property.")


    @property
    def parallelisation(self):
        """Gets value of {class-name} parallelisation property."""
        return self.__parallelisation

    @parallelisation.setter
    def parallelisation(self, value):
        if value is not None and not isinstance(value, Parallelisation):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} parallelisation property."""
        self.__parallelisation = value

    @parallelisation.deleter
    def parallelisation(self, value):
        """Deletes {class-name} parallelisation property."""
        raise TypeError("Cannot delete {class-name} parallelisation property.")


    @property
    def platform(self):
        """Gets value of {class-name} platform property.

        The platform that this deployment has been run on. It is optional to allow for "unconfigured" models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS)."""
        return self.__platform

    @platform.setter
    def platform(self, value):
        if value is not None and not isinstance(value, Platform):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} platform property."""
        self.__platform = value

    @platform.deleter
    def platform(self, value):
        """Deletes {class-name} platform property."""
        raise TypeError("Cannot delete {class-name} platform property.")


    @property
    def platform_reference(self):
        """Gets value of {class-name} platform_reference property."""
        return self.__platform_reference

    @platform_reference.setter
    def platform_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} platform_reference property."""
        self.__platform_reference = value

    @platform_reference.deleter
    def platform_reference(self, value):
        """Deletes {class-name} platform_reference property."""
        raise TypeError("Cannot delete {class-name} platform_reference property.")



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
        append(d, 'deployment_date', self.__deployment_date, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'executable_arguments', self.__executable_arguments, True, True, False)
        append(d, 'executable_name', self.__executable_name, False, True, False)
        append(d, 'parallelisation', self.__parallelisation, False, False, False)
        append(d, 'platform', self.__platform, False, False, False)
        append(d, 'platform_reference', self.__platform_reference, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = Deployment()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Deployment', e)
