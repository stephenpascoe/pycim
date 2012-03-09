"""CIM json encoding functions.

"""

# Module imports.
import datetime
import simplejson
import uuid

from pycim.core.cim_exception import CIMException
from pycim.core.cim_constants import CIM_VERSIONS


# Module exports.
__all__ = ['encode']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


class JSONEncoder(simplejson.JSONEncoder):
    """
    Extends simplejson to handle specific types.
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat().replace('T', ' ')
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            return simplejson.JSONEncoder.default(self, obj)


def encode(instance, version):
    """Encodes an yaml representation of passed CIM instance.

    Keyword arguments:
    instance -- instance of a CIM type.
    version -- cim version that instance conforms to.

    """
    # Defensive programming.
    if instance is None:
        raise CIMException('Cannot encode null instances.')
    if version not in CIM_VERSIONS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))

    # Convert dictionary representation of instance.
    d = instance.as_dict()
    return JSONEncoder().encode(d)
