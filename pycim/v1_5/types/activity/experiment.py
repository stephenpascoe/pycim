"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.191878.
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
from pycim.v1_5.types.activity.activity import Activity
from pycim.v1_5.types.activity.measurement_campaign import MeasurementCampaign
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.shared.cim_reference import CimReference



# Module exports.
__all__ = ['Experiment']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.191878$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Experiment(Activity):
    """An abstract class within the cim v1.5 type system.

    An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Experiment, self).__init__()

        self.__generates = []                                       # type = str
        self.__measurement_campaigns = []                           # type = activity.MeasurementCampaign
        self.__requires = []                                        # type = activity.NumericalActivity
        self.__requires_references = []                             # type = shared.CimReference
        self.__supports = []                                        # type = str
        self.__supports_references = []                             # type = shared.CimReference


    @property
    def generates(self):
        """Gets value of {class-name} generates property."""
        return list(self.__generates)

    @generates.setter
    def generates(self, value):
        """Sets value of {class-name} generates property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__generates = []
        for i in value:
            self.append_to_generates(i)

    @generates.deleter
    def generates(self, value):
        """Deletes {class-name} generates property."""
        raise TypeError("Cannot delete {class-name} generates property.")

    def append_to_generates(self, item):
        """Appends an item to the managed {class-name} generates collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__generates.append(item)

    def remove_from_generates(self, item):
        """Removes an item from the managed {class-name} generates collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__generates.remove(item)


    @property
    def measurement_campaigns(self):
        """Gets value of {class-name} measurement_campaigns property."""
        return list(self.__measurement_campaigns)

    @measurement_campaigns.setter
    def measurement_campaigns(self, value):
        """Sets value of {class-name} measurement_campaigns property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__measurement_campaigns = []
        for i in value:
            self.append_to_measurement_campaigns(i)

    @measurement_campaigns.deleter
    def measurement_campaigns(self, value):
        """Deletes {class-name} measurement_campaigns property."""
        raise TypeError("Cannot delete {class-name} measurement_campaigns property.")

    def append_to_measurement_campaigns(self, item):
        """Appends an item to the managed {class-name} measurement_campaigns collection."""
        if not isinstance(item, MeasurementCampaign):
            raise TypeError("item is of incorrect type.")
        self.__measurement_campaigns.append(item)

    def remove_from_measurement_campaigns(self, item):
        """Removes an item from the managed {class-name} measurement_campaigns collection."""
        if not isinstance(item, MeasurementCampaign):
            raise TypeError("item is of incorrect type.")
        self.__measurement_campaigns.remove(item)


    @property
    def requires(self):
        """Gets value of {class-name} requires property."""
        return list(self.__requires)

    @requires.setter
    def requires(self, value):
        """Sets value of {class-name} requires property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__requires = []
        for i in value:
            self.append_to_requires(i)

    @requires.deleter
    def requires(self, value):
        """Deletes {class-name} requires property."""
        raise TypeError("Cannot delete {class-name} requires property.")

    def append_to_requires(self, item):
        """Appends an item to the managed {class-name} requires collection."""
        if not isinstance(item, NumericalActivity):
            raise TypeError("item is of incorrect type.")
        self.__requires.append(item)

    def remove_from_requires(self, item):
        """Removes an item from the managed {class-name} requires collection."""
        if not isinstance(item, NumericalActivity):
            raise TypeError("item is of incorrect type.")
        self.__requires.remove(item)


    @property
    def requires_references(self):
        """Gets value of {class-name} requires_references property."""
        return list(self.__requires_references)

    @requires_references.setter
    def requires_references(self, value):
        """Sets value of {class-name} requires_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__requires_references = []
        for i in value:
            self.append_to_requires_references(i)

    @requires_references.deleter
    def requires_references(self, value):
        """Deletes {class-name} requires_references property."""
        raise TypeError("Cannot delete {class-name} requires_references property.")

    def append_to_requires_references(self, item):
        """Appends an item to the managed {class-name} requires_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__requires_references.append(item)

    def remove_from_requires_references(self, item):
        """Removes an item from the managed {class-name} requires_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__requires_references.remove(item)


    @property
    def supports(self):
        """Gets value of {class-name} supports property."""
        return list(self.__supports)

    @supports.setter
    def supports(self, value):
        """Sets value of {class-name} supports property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__supports = []
        for i in value:
            self.append_to_supports(i)

    @supports.deleter
    def supports(self, value):
        """Deletes {class-name} supports property."""
        raise TypeError("Cannot delete {class-name} supports property.")

    def append_to_supports(self, item):
        """Appends an item to the managed {class-name} supports collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__supports.append(item)

    def remove_from_supports(self, item):
        """Removes an item from the managed {class-name} supports collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__supports.remove(item)


    @property
    def supports_references(self):
        """Gets value of {class-name} supports_references property."""
        return list(self.__supports_references)

    @supports_references.setter
    def supports_references(self, value):
        """Sets value of {class-name} supports_references property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__supports_references = []
        for i in value:
            self.append_to_supports_references(i)

    @supports_references.deleter
    def supports_references(self, value):
        """Deletes {class-name} supports_references property."""
        raise TypeError("Cannot delete {class-name} supports_references property.")

    def append_to_supports_references(self, item):
        """Appends an item to the managed {class-name} supports_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__supports_references.append(item)

    def remove_from_supports_references(self, item):
        """Removes an item from the managed {class-name} supports_references collection."""
        if not isinstance(item, CimReference):
            raise TypeError("item is of incorrect type.")
        self.__supports_references.remove(item)



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
        d = dict(super(Experiment, self).as_dict())
        append(d, 'generates', self.__generates, True, True, False)
        append(d, 'measurement_campaigns', self.__measurement_campaigns, True, False, False)
        append(d, 'requires', self.__requires, True, False, False)
        append(d, 'requires_references', self.__requires_references, True, False, False)
        append(d, 'supports', self.__supports, True, True, False)
        append(d, 'supports_references', self.__supports_references, True, False, False)
        return d






# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.
from pycim.v1_5.types.activity.numerical_activity import NumericalActivity


