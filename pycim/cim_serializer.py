"""Exposes functions for decoding/encoding cim instances.

"""

# Module imports.
from pycim.core.cim_exception import CIMException
from pycim.core.cim_constants import CIM_ENCODINGS
from pycim.core.cim_constants import CIM_VERSIONS
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
    if version not in CIM_VERSIONS:
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
    if version not in CIM_VERSIONS:
        raise CIMException('{0} is an unsupported CIM version.'.format(version))
    if encoding not in CIM_ENCODINGS:
        raise CIMException('{0} is an unsupported CIM encoding.'.format(encoding))

    # print "... encoding cim instance to {0}".format(encoding)
    return encode_representation(instance, version, encoding)



if __name__ == '__main__':
    representation = '/Users/markmorgan/Development/metafor/cim_software/trunk/python/src/cim_test/cim_test/v1_5/test_data/data_object.xml'
    print representation
    instance = decode(representation, '1.5', 'xml')
    print "CIM DECODING TEST - 1"
    print "... representation      : {0}".format(representation)
    print "... representation type : xml"
    print "... entity              : {0}".format(instance)
    print "... entity id           : {0}".format(instance.cim_info.id)
    print "... entity version      : {0}".format(instance.cim_info.version)
    print "... entity create_date  : {0}".format(instance.cim_info.create_date)
    print "... data object purpose                 : {0}".format(instance.purpose)
    print "... data object hierarchy_level name    : {0}".format(instance.hierarchy_level.name)
    print "... data object hierarchy_level value   : {0}".format(instance.hierarchy_level.value)
    print "... data object hierarchy_level is_open : {0}".format(instance.hierarchy_level.is_open)

    print "CIM DECODING TEST - 2"
    as_base64 = encode(instance, '1.5', 'base64')
    from_base64 = decode(as_base64, '1.5', 'base64')

    as_binary = encode(instance, '1.5', 'binary')
    from_binary = decode(as_binary, '1.5', 'binary')

    as_json = encode(instance, '1.5', 'json')
    from_json = decode(as_json, '1.5', 'json')

    as_yaml = encode(instance, '1.5', 'yaml')
    from_yaml = decode(as_yaml, '1.5', 'yaml')

#    as_xml = encode(instance, '1.5', 'xml')
#    from_xml = decode(as_xml, '1.5', 'xml')
