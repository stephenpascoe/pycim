"""A cim unit test utility class.

"""

# Module imports.
import sys

from lxml import etree as et


# Module provenance info.
__author__="markmorgan"
__date__ ="$Aug 31, 2010 11:43:27 AM$"
__copyright__ = "Copyright 2011 - Metafor Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


def get_test_file_path(file_name, cim_version='v1_5'):
    """Returns file path for a test file.

    """
    for path in sys.path:
        if path.endswith('pycim_test'):
            return path + '/' + cim_version + '/test_data/' + file_name
    return None


def get_test_xml_file(file_name, cim_version='v1_5'):
    """Opens & returns a test xml file.

    """
    path = get_test_file_path(file_name, cim_version)
    return et.parse(path)


def do_representation_test_from_xml_file(xml_file, version, encoding):
    """Opens & returns a test xml file.

    Keyword Arguments:
    xml_file - name of xml file to be opened.
    version -- cim version that representation conforms to.
    encoding -- type of representation to decode.

    """
    from pycim.cim_serializer import decode, encode

    # Decode from xml test file.
    xml = get_test_xml_file(xml_file)
    obj = decode(xml, version, 'xml')

    # Encode.
    encoded = encode(obj, version, encoding)
    assert encoded is not None

    # Decode.
    decoded = decode(encoded, version, encoding)
    assert decoded is not None

    # Compare decodings.
    assert obj.as_dict() == decoded.as_dict()
    
    