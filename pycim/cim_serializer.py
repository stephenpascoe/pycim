"""Exposes functions for decoding/encoding cim instances.

"""

# Module imports.
from pycim.core.cim_exception import CIMException
from pycim.cim_constants import CIM_ENCODINGS
from pycim.cim_constants import CIM_SCHEMAS
from pycim.core.decoding.cim_decoder import decode as decode_instance
from pycim.core.encoding.cim_encoder import encode as encode_representation

# Module exports.
__all__ = ['decode', 'encode']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



def decode(representation, version, encoding):
    """Decodes a CIM instance from passed representation & encoding.

    Keyword arguments:
    representation -- a representation of a CIM instance.
    version -- cim version that representation conforms to.
    encoding -- type of representation to decode.

    """
    # Defensive programming.
    if representation is None:
        raise CIMException('CIM instances cannot be decoded from null objects.')
    if version not in CIM_SCHEMAS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))
    if encoding not in CIM_ENCODINGS:
        raise CIMException('{0} is an unsupported CIM encoding.'.format(encoding))

    # print "... decoding cim instance from {0}".format(encoding)
    return decode_instance(representation, version, encoding)


def encode(instance, version, encoding):
    """Encodes a representation of passed encoding from passed CIM instance.

    Keyword arguments:
    instance -- instance of a CIM type.
    version -- cim version that instance conforms to.
    encoding -- type of representation to encode.

    """
    # Defensive programming.
    if instance is None:
        raise CIMException('Cannot encode null objects.')
    if version not in CIM_SCHEMAS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))
    if encoding not in CIM_ENCODINGS:
        raise CIMException('{0} is an unsupported CIM encoding.'.format(encoding))

    # print "... encoding cim instance to {0}".format(encoding)
    return encode_representation(instance, version, encoding)


