"""CIM binary encoding functions.

"""

# Module imports.
import base64

from pycim.core.cim_exception import CIMException
from pycim.cim_constants import CIM_SCHEMAS
from pycim.core.encoding.cim_encoder_binary import encode as encode_to_binary

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


def encode(instance, version):
    """Encodes a binary representation of passed CIM instance.

    Keyword arguments:
    instance -- instance of a CIM type.
    version -- cim version that instance conforms to.

    """
    # Defensive programming.
    if instance is None:
        raise CIMException('Cannot encode null instances.')
    if version not in CIM_SCHEMAS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))

    as_binary = encode_to_binary(instance, version)
    return base64.b64encode(as_binary)
