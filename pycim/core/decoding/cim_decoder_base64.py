"""CIM binary decoding functions.

"""

# Module imports.
import base64

from pycim.core.cim_exception import CIMException
from pycim.cim_constants import CIM_SCHEMAS
from pycim.core.decoding.cim_decoder_binary import decode as decode_from_binary


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
    """Decodes a CIM instance from passed base64 representation.

    Keyword arguments:
    representation -- a base64 representation of a CIM instance.

    """
    # Defensive programming.
    if representation is None:
        raise CIMException('Cannot decode null representations.')
    if version not in CIM_SCHEMAS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))

    as_binary_string = base64.b64decode(representation)
    return decode_from_binary(as_binary_string, version)

