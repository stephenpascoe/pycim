"""Exposes functions for encoding representations from cim instances.

"""

# Module imports.
from pycim.core.cim_exception import CIMException
from pycim.core.cim_constants import CIM_ENCODINGS
from pycim.core.cim_constants import CIM_VERSIONS
from pycim.core.encoding.cim_encoder_base64 import encode as encode_to_base64
from pycim.core.encoding.cim_encoder_binary import encode as encode_to_binary
from pycim.core.encoding.cim_encoder_json import encode as encode_to_json
from pycim.core.encoding.cim_encoder_xml import encode as encode_to_xml
from pycim.core.encoding.cim_encoder_yaml import encode as encode_to_yaml

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



# Set of encoders by encoding type.
_encoders = {
    'base64' : encode_to_base64,
    'binary' : encode_to_binary,
    'json' : encode_to_json,
    'xml' : encode_to_xml,
    'yaml' : encode_to_yaml,
}


def encode(instance, version, encoding):
    """Encodes a representation of passed encoding from passed CIM instance.

    Keyword arguments:
    instance -- instance of a CIM type.
    version -- cim version that instance conforms to.
    encoding -- type of representation to encode.

    """
    # Defensive programming.
    if instance is None:
        raise CIMException('Cannot encode null instances.')
    if version not in CIM_VERSIONS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))
    if encoding not in CIM_ENCODINGS:
        raise CIMException('{0} is an unsupported CIM encoding.'.format(encoding))

    # Encode instance to representation.
    return _encoders[encoding](instance, version)

