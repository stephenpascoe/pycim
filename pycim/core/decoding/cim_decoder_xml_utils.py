"""CIM xml decoding utility functions.

"""

# Module imports.
import uuid
import datetime
import types

from dateutil import parser as dateutil_parser
from lxml import etree as et
from lxml.etree import _ElementStringResult as etstring

from pycim.core.cim_exception import CIMException


# Module exports.
__all__ = ["convert_to_string", 
           "convert_to_bool",
           "convert_to_integer",
           "convert_to_float",
           "convert_to_uid",
           "convert_to_datetime",
           "set_attributes",
           "decode_xml",
           "get_cim_xml"]


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Null uuid for checking whether one has to be generated.
NULL_UUID = ['00000000-0000-0000-0000-000000000000']



def _get_value_as_string(xml, nsmap):
    """Converts passed xml fragment to a string.

    Keyword Arguments:
    xml - an xml element.
    nsmap -- set of xml namespace mappings.

    """
    # Strip first item from iterables.
    if isinstance(xml, types.ListType):
        if len(xml) > 0:
            xml = xml[0]
        else:
            xml = None

    if xml is None:
        return None
    elif isinstance(xml, types.StringTypes):
        return xml.encode('utf-8', 'ignore')
    else:
        return et.tostring(xml)


def convert_to_string(xml, nsmap=None):
    """Converts an etree element xml representation into a string type.

    Keyword Arguments:
    xml - an etree xml element.
    nsmap -- set of xml namespace mappings.

    """
    as_string = _get_value_as_string(xml, nsmap)
    return as_string

def convert_to_bool(xml, nsmap=None):
    """Converts an etree element xml representation into a boolean type.

    Keyword Arguments:
    xml - an etree xml element.
    nsmap -- set of xml namespace mappings.

    """
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is not None:
        as_string = as_string.upper()
        if as_string in ['TRUE']:
            return True
        elif as_string in ['FALSE']:
            return False
    return bool(as_string)


def convert_to_integer(xml, nsmap=None):
    """Converts an etree element xml representation into an integer type.

    Keyword Arguments:
    xml - an etree xml element.
    nsmap -- set of xml namespace mappings.

    """
    as_string = _get_value_as_string(xml, nsmap)
    return int(as_string)


def convert_to_float(xml, nsmap=None):
    """Converts an etree element xml representation into a float type.

    Keyword Arguments:
    xml - an etree xml element.
    nsmap -- set of xml namespace mappings.

    """
    as_string = _get_value_as_string(xml, nsmap)
    return float(as_string)


def convert_to_uid(xml, nsmap=None):
    """Converts an etree element xml representation into a uid type.

    Keyword Arguments:
    xml - an etree xml element.
    nsmap -- set of xml namespace mappings.

    """
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None or as_string in NULL_UUID:
        return uuid.uuid4()
    else:
        return uuid.UUID(as_string)


def convert_to_datetime(xml, nsmap=None):
    """Converts an etree element xml representation into a datetime type.

    Keyword Arguments:
    xml - an etree xml element.
    nsmap -- set of xml namespace mappings.

    """
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None:
        return None
    else:
        return dateutil_parser.parse(as_string)


# Set of simple type convertors.
_simple_type_decoders = {
    'bool' : convert_to_bool,
    'date' : convert_to_datetime,
    'datetime' : convert_to_datetime,
    'float' : convert_to_float,
    'int' : convert_to_integer,
    'str' : convert_to_string,
    'uri' : convert_to_string,
    'uuid' : convert_to_uid,
}


def set_attributes(target, xml, nsmap, decodings):
    """Decodes entity attributes from a collection of decodings.

    Keyword arguments:
    target -- an object with a set of attributes to be assigned.
    xml -- etree xml element from which attribute values are decoded.
    decodings -- set of mappings used to perform decoding.

    """

    # Iterate & apply decodings.
    for decoding in decodings:
        # N.B. attributes to be ommitted can be declared as a mnemonic.
        if len(decoding) == 1:
            pass
        elif len(decoding) == 4:
            attr, is_iterable, type, xpath  = decoding
            is_simple_type = type in _simple_type_decoders
            try:
                _set_attribute(target, xml, nsmap, attr, type, xpath, is_simple_type, is_iterable)
            except Exception as e:
                print attr, is_iterable, type, is_simple_type, xpath, e

    # Support operation chaining.
    return target


def _set_attribute(target, xml, nsmap, attr, decoder, xpath, is_simple_type, is_iterable):
    """Decodes entity attributes from a collection of decodings.

    Keyword arguments:
    target -- an object with an attribute to be assigned.
    xml -- etree xml element from which attribute value is decoded.
    nsmap -- xml namespace mappings.
    attr -- attribute to be assigned.
    decoder -- attribute decoder.
    xpath -- attribute xpath.
    is_simple_type -- flag indicating whether type is a simple one or not.
    is_iterable -- flag indicating whether attribute is iterable or not.

    """
    # Set target object / attribute.
    obj = target
    parts = attr.split('.')
    for i in range(len(parts) - 1):
        obj = getattr(obj, parts[i])
    att_name = parts[len(parts) - 1]

    # Get attribute value.
    att_value = _get_attribute_value(xml, nsmap, decoder, xpath, is_simple_type, is_iterable)

    # Set attribute value.
    if not is_iterable:
        if is_simple_type:
            setattr(obj, att_name, att_value)
        else:
            # ... do not overwrite previously assigned property values.
            cur_obj = getattr(obj, att_name)
            if cur_obj is None:
                setattr(obj, att_name, att_value)
    else:
        if len(att_value) > 0:
            m = getattr(obj, 'append_to_' + att_name)
            for i in att_value:
                m(i)

    # Support operation chaining.
    return target


def _get_attribute_value(xml, nsmap, decoder, xpath, is_simple_type, is_iterable):
    """Gets the value of an attribute from xml.

    Keyword arguments:
    xml -- etree xml element from which attribute value is decoded.
    nsmap -- xml namespace mappings.
    decoder -- attribute decoder.
    xpath -- attribute xpath.
    is_simple_type -- flag indicating whether attribute type is a simple one or not.
    is_iterable -- flag indicating whether attribute type is iterable or not.

    """
    result = None

    # Apply xpath (derive xml fragment from value is derived).
    att_xml = xml.xpath(xpath, namespaces=nsmap)

    # From xml derive value.
    # ... simple types.
    if is_simple_type == True:
        if decoder in _simple_type_decoders:
            decoder = _simple_type_decoders[decoder]
        if is_iterable:
            result = []
            for el in att_xml:
                result.append(decoder(el, nsmap))
        else:
            result = decoder(att_xml, nsmap)

    # ... complex types.
    else:
        result = decode_xml(decoder, att_xml, nsmap, is_iterable)

    return result


def decode_xml(decoder, xml, nsmap, is_iterable):
    """Decodes either an entity or an entity collection from xml.

    Keyword arguments:
    decoder -- function to decode an entity instance.
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.
    take_first -- flag indicating whether to return only the first entity of a collection.

    """
    # None if passed none.
    if xml is None:
        # print 'Nothing to decode ...'
        return None

    # Instance if passed etree element.
    if isinstance(xml, et._Element):
        # print 'Decoding an instance ...'
        return decoder(xml, nsmap)

    # Instance if passed etree element collection and caller wants first only.
    if isinstance(xml, types.ListType) and is_iterable == False:
        # print 'Decoding first instance  from collection ...'
        return None if len(xml) == 0 else decode_xml(decoder, xml[0], nsmap, None)

    # Collection if passed etree element collection.
    if isinstance(xml, types.ListType):
        # print 'Decoding a collection ...'
        collection = []
        for elem in xml:
            instance = decode_xml(decoder, elem, nsmap, None)
            collection.append(instance)
        return collection

    # otherwise exception
    raise CIMException("xml cannot be decoded.")
    

def get_cim_xml(xml, return_nsmap=False):
    """Deserializes cim instance to an etree element.

    Keyword arguments:
    xml -- an xml representation of a cim instance.
    return_nsmap -- flag indicating whether namespace map will be returned or not.

    """
    # Defensive programming.
    if xml is None:
        raise CIMException("CIM instance as xml is undefined.")

    nsmap = None
    # ... etree elements.
    if isinstance(xml, et._Element):
        nsmap = xml.nsmap
    # ... etree element trees.
    elif isinstance(xml, et._ElementTree):
        xml = xml.getroot()
        nsmap = xml.nsmap
    else:
        # ... files / URLs.
        try:
            xml = et.parse(xml)
            xml = xml.getroot()
            nsmap = xml.nsmap
        except Exception as e:
            # ... strings.
            if isinstance(xml, basestring):
                try:
                    xml = et.fromstring(xml)
                    nsmap = xml.nsmap
                except Exception:
                    raise CIMException("Invalid cim instance xml string.")
            else:
                raise CIMException("Unsupported cim_instance xml type, must be either a string, file, url or etree.")

    # Guarantees that cim is default namespace.
    if nsmap is not None:
        nsmap['cim'] = nsmap.pop(None)

    # Return either a tuple or single.
    if return_nsmap == True:
        return xml, nsmap
    else:
        return xml


