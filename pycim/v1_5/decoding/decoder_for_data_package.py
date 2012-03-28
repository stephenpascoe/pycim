"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 16:29:10.556443.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.decoding.decoder_for_shared_package import *
from pycim.v1_5.types.data import *


# Module exports.
__all__ = [
    "decode_data_content", 
    "decode_data_distribution", 
    "decode_data_extent", 
    "decode_data_extent_geographical", 
    "decode_data_extent_temporal", 
    "decode_data_extent_time_interval", 
    "decode_data_hierarchy_level", 
    "decode_data_object", 
    "decode_data_property", 
    "decode_data_restriction", 
    "decode_data_storage", 
    "decode_data_storage_db", 
    "decode_data_storage_file", 
    "decode_data_storage_ip", 
    "decode_data_topic"
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-28 16:29:10.556443"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_data_content(xml, nsmap):
    """Decodes a data content instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('aggregation', False, 'str', 'child::cim:aggregation/text()'),
        ('frequency', False, 'str', 'child::cim:frequency/@value'),
        ('topic', False, decode_data_topic, 'child::cim:topic'),
    ]

    return set_attributes(DataContent(), xml, nsmap, decodings)


def decode_data_distribution(xml, nsmap):
    """Decodes a data distribution instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('access', False, 'str', '@distributionAccess'),
        ('format', False, 'str', 'child::cim:distributionFormat/@value'),
        ('responsible_party', False, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(DataDistribution(), xml, nsmap, decodings)


def decode_data_extent(xml, nsmap):
    """Decodes a data extent instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('geographical', False, decode_data_extent_geographical, 'child::gmd:geographicElement'),
        ('temporal', False, decode_data_extent_temporal, 'child::gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod'),
    ]

    return set_attributes(DataExtent(), xml, nsmap, decodings)


def decode_data_extent_geographical(xml, nsmap):
    """Decodes a data extent geographical instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('east', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal/text()'),
        ('north', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal/text()'),
        ('south', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal/text()'),
        ('west', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal/text()'),
    ]

    return set_attributes(DataExtentGeographical(), xml, nsmap, decodings)


def decode_data_extent_temporal(xml, nsmap):
    """Decodes a data extent temporal instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('begin', False, 'date', 'child::gml:beginPosition/text()'),
        ('end', False, 'date', 'child::gml:endPosition/text()'),
        ('time_interval', False, decode_data_extent_time_interval, 'child::gml:timeInterval'),
    ]

    return set_attributes(DataExtentTemporal(), xml, nsmap, decodings)


def decode_data_extent_time_interval(xml, nsmap):
    """Decodes a data extent time interval instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('factor', False, 'int', '@factor'),
        ('radix', False, 'int', '@radix'),
        ('unit', False, 'str', '@unit'),
    ]

    return set_attributes(DataExtentTimeInterval(), xml, nsmap, decodings)


def decode_data_hierarchy_level(xml, nsmap):
    """Decodes a data hierarchy level instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('is_open', False, 'bool', 'child::cim:hierarchyLevelName/@open'),
        ('name', False, 'str', 'child::cim:hierarchyLevelName/@value'),
        ('value', False, 'str', 'child::cim:hierarchyLevelValue/text()'),
    ]

    return set_attributes(DataHierarchyLevel(), xml, nsmap, decodings)


def decode_data_object(xml, nsmap):
    """Decodes a data object instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('acronym', False, 'str', 'child::cim:acronym/text()'),
        ('cim_info', False, decode_cim_info, 'self::cim:dataObject'),
        ('citations', True, decode_citation, '//cim:citation[not(cim:citation)]'),
        ('content', True, decode_data_content, 'child::cim:content'),
        ('data_property', True, decode_data_property, 'child::cim:dataProperty/cim:dataProperty'),
        ('data_status', False, 'str', 'self::cim:dataObject/@dataStatus'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('distribution', False, decode_data_distribution, 'child::cim:distribution'),
        ('extent', False, decode_data_extent, 'child::cim:extent'),
        ('hierarchy_level', False, decode_data_hierarchy_level, 'self::cim:dataObject'),
        ('keyword', False, 'str', 'child::cim:keyword/text()'),
        ('purpose', False, 'str', 'self::cim:dataObject/@purpose'),
    ]

    return set_attributes(DataObject(), xml, nsmap, decodings)


def decode_data_property(xml, nsmap):
    """Decodes a data property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('value', False, 'str', 'child::cim:value/text()'),
    ]

    return set_attributes(DataProperty(), xml, nsmap, decodings)


def decode_data_restriction(xml, nsmap):
    """Decodes a data restriction instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(DataRestriction(), xml, nsmap, decodings)


def decode_data_storage(xml, nsmap):
    """Decodes a data storage instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(DataStorage(), xml, nsmap, decodings)


def decode_data_storage_db(xml, nsmap):
    """Decodes a data storage db instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(DataStorageDb(), xml, nsmap, decodings)


def decode_data_storage_file(xml, nsmap):
    """Decodes a data storage file instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(DataStorageFile(), xml, nsmap, decodings)


def decode_data_storage_ip(xml, nsmap):
    """Decodes a data storage ip instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(DataStorageIp(), xml, nsmap, decodings)


def decode_data_topic(xml, nsmap):
    """Decodes a data topic instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('unit', False, 'str', 'child::cim:unit/@value'),
    ]

    return set_attributes(DataTopic(), xml, nsmap, decodings)


