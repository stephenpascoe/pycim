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


def get_test_file_path(version, file_name):
    """Returns file path for a test file.

    """
    for path in sys.path:
        if path.endswith('pycim/tests'):
            return path + '/pycim_test/v' + version.replace('.', '_') + '/test_data/' + file_name
    return None


def get_test_xml_file(version, file_name):
    """Opens & returns a test xml file.

    
    """
    path = get_test_file_path(version, file_name)
    return et.parse(path)


def decode_obj_from_xml(version, xml_file, expected_type):
    """Decodes a test xml file & performs basic assertions.

    Keyword Arguments:
    version -- cim version that representation conforms to.
    xml_file - name of xml file to be opened.
    expected_type -- type that the decoded instance should be.

    """
    from pycim.cim_serializer import decode

    # Open cim xml file.
    xml = get_test_xml_file(version, xml_file)

    # Decode.
    obj = decode(xml, version, 'xml')

    # Perform basic assertions.
    assert obj is not None
    assert isinstance(obj, expected_type)

    return obj


def decode_dict_from_xml(version, xml_file, expected_type):
    """Decodes a dictionary from xml file.

    Keyword Arguments:
    version -- cim version that representation conforms to.
    xml_file - name of xml file to be opened.
    expected_type -- type that the decoded instance should be.

    """
    obj = decode_obj_from_xml(version, xml_file, expected_type)

    # Convert.
    d = obj.as_dict()

    # Perform basic assertions.
    assert d is not None
    assert isinstance(d, dict)

    return d


def do_test_from_xml_file(version, xml_file, encoding):
    """Tests an xml representation aginst passed encoding.

    Keyword Arguments:
    version -- cim version that representation conforms to.
    xml_file - name of xml file to be opened.
    encoding -- type of representation to decode.

    """
    from pycim.cim_serializer import decode, encode

    # Decode from xml test file.
    xml = get_test_xml_file(version, xml_file)
    obj = decode(xml, version, 'xml')

    # Encode.
    encoded = encode(obj, version, encoding)
    assert encoded is not None

    # Decode.
    decoded = decode(encoded, version, encoding)
    assert decoded is not None

    # Compare decodings.
    assert obj.as_dict() == decoded.as_dict()
    
    