"""CIM binary decoding functions.

"""

# Module imports.
import pickle

from pycim.core.cim_exception import CIMException
from pycim.core.cim_constants import CIM_VERSIONS


# Module exports.
__all__ = ['decode']


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
    """Decodes a CIM instance from passed binary representation.

    Keyword arguments:
    representation -- a binary representation of a CIM instance.

    """
    # Defensive programming.
    if representation is None:
        raise CIMException('Cannot decode null representations.')
    if version not in CIM_VERSIONS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))

    obj = pickle.loads(representation)
    return obj

