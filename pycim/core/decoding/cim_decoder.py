"""Exposes functions for decoding cim instances from representations.

"""

# Module imports.
from pycim.core.cim_exception import CIMException
from pycim.cim_constants import CIM_ENCODINGS
from pycim.cim_constants import CIM_SCHEMAS
from pycim.core.decoding.cim_decoder_base64 import decode as decode_from_base64
from pycim.core.decoding.cim_decoder_binary import decode as decode_from_binary
from pycim.core.decoding.cim_decoder_json import decode as decode_from_json
from pycim.core.decoding.cim_decoder_xml import decode as decode_from_xml

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


# Set of decoders by encoding type.
_decoders = {
    'base64' : decode_from_base64,
    'binary' : decode_from_binary,
    'json' : decode_from_json,
    'xml' : decode_from_xml,
}


def decode(representation, version, encoding):
    """Decodes a CIM instance from passed representation & encoding.

    Keyword arguments:
    representation -- a representation of a CIM instance.
    version -- cim version that representation conforms to.
    encoding -- type of representation to decode.

    """
    # Defensive programming.
    if representation is None:
        raise CIMException('Cannot decode null representations.')
    if version not in CIM_SCHEMAS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))
    if encoding not in CIM_ENCODINGS:
        raise CIMException('{0} is an unsupported CIM encoding.'.format(encoding))

    # Decode instance from representation.
    return _decoders[encoding](representation, version)


