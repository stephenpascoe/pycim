"""CIM json decoding functions.

"""

# Module imports.
import simplejson

from pycim.core.cim_exception import CIMException
from pycim.core.cim_constants import CIM_VERSIONS

# Module exports.
_all__ = ['decode']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode(representation, version):
    """Decodes a CIM instance from passed v representation.

    Keyword arguments:
    representation -- a yaml representation of a CIM instance.

    """
    # Defensive programming.
    if representation is None:
        raise CIMException('Cannot decode null representations.')
    if version not in CIM_VERSIONS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))

    as_dict = simplejson.loads(representation)
    
    # TODO convert dictionary to object.
    return as_dict
