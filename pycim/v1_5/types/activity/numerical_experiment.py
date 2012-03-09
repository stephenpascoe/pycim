"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-02-15 15:48:21.228531.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['NumericalExperiment']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-02-15 15:48:21.228531$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class NumericalExperiment(object):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(NumericalExperiment, self).__init__()

        self.__name = None                                          # type = str


    @property
    def name(self):
        """Gets value of {class-name} name property."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes {class-name} name property."""
        raise TypeError("Cannot delete {class-name} name property.")



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
        append(d, 'name', self.__name, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = NumericalExperiment()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.NumericalExperiment', e)
