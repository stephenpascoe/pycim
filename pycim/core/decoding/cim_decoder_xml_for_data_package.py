"""A set of xml decoding functions for the data CIM sub-package.

"""

# Module imports.
from pycim.v1_5.types.data import *
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.core.decoding.cim_decoder_xml_for_shared_package import *


# Module exports.
__all__ = ['decode_data_object']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



def decode_data_object(xml, nsmap):
    """Decodes a data object instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('acronym', 'child::cim:acronym/text()', 'str', False),
        ('cim_info', 'self::cim:dataObject', decode_cim_info, False),
        ('citations', '//cim:citation[not(cim:citation)]', decode_citation, True),
        ('content', 'child::cim:content', decode_data_content, True),
        ('data_property', 'child::cim:dataProperty/cim:dataProperty', decode_data_property, True),
        ('data_status', 'self::cim:dataObject/@dataStatus', 'str', False),
        ('description', 'child::cim:description/text()', 'str', False),
        ('distribution', 'child::cim:distribution', decode_data_distribution, False),
        ('extent', 'child::cim:extent', decode_data_extent, False),
        ('hierarchy_level', 'self::cim:dataObject', decode_data_hierarchy_level, False),
        ('keyword', 'child::cim:keyword/text()', 'str', False),
        ('purpose', 'self::cim:dataObject/@purpose', 'str', False),
    ]

    return set_attributes(DataObject(), xml, nsmap, decodings)


def decode_data_hierarchy_level(xml, nsmap):
    """Decodes a data hierarchy level instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('is_open', 'child::cim:hierarchyLevelName/@open', 'bool', False),
        ('name', 'child::cim:hierarchyLevelName/@value', 'str', False),
        ('value', 'child::cim:hierarchyLevelValue/text()', 'str', False),
    ]

    return set_attributes(DataHierarchyLevel(), xml, nsmap, decodings)


def decode_data_distribution(xml, nsmap):
    """Decodes a data distribution instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('access', '@distributionAccess', 'str', False),
        ('format', 'child::cim:distributionFormat/@value', 'str', False),
        ('responsible_party', 'child::cim:responsibleParty', decode_responsible_party, False),
    ]

    return set_attributes(DataDistribution(), xml, nsmap, decodings)


def decode_data_extent(xml, nsmap):
    """Decodes a data extent instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('geographical', 'child::gmd:geographicElement', decode_data_extent_geographical, False),
        ('temporal', 'child::gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod', decode_data_extent_temporal, False),
    ]

    return set_attributes(DataExtent(), xml, nsmap, decodings)


def decode_data_extent_geographical(xml, nsmap):
    """Decodes a data extent geographical instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('east', 'child::gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal/text()', 'float', False),
        ('south', 'child::gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal/text()', 'float', False),
        ('west', 'child::gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal/text()', 'float', False),
        ('north', 'child::gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal/text()', 'float', False),
    ]

    return set_attributes(DataExtentGeographical(), xml, nsmap, decodings)


def decode_data_extent_temporal(xml, nsmap):
    """Decodes a data extent temporal instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('begin', 'child::gml:beginPosition/text()', 'datetime', False),
        ('end', 'child::gml:endPosition/text()', 'datetime', False),
        ('time_interval', 'child::gml:timeInterval', decode_data_extent_time_interval, False),
    ]

    return set_attributes(DataExtentTemporal(), xml, nsmap, decodings)



def decode_data_extent_time_interval(xml, nsmap):
    """Decodes a data extent time interval instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('factor', '@factor', 'int', False),
        ('radix', '@radix', 'int', False),
        ('unit', '@unit', 'str', False),
    ]

    return set_attributes(DataExtentTimeInterval(), xml, nsmap, decodings)


def decode_data_content(xml, nsmap):
    """Decodes a data content instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('aggregation', 'child::cim:aggregation/text()', 'str', False),
        ('frequency', 'child::cim:frequency/@value', 'str', False),
        ('topic', 'child::cim:topic', decode_data_topic, False),
    ]

    return set_attributes(DataContent(), xml, nsmap, decodings)


def decode_data_topic(xml, nsmap):
    """Decodes a data topic instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', 'child::cim:description/text()', 'str', False),
        ('name', 'child::cim:name/text()', 'str', False),
        ('unit', 'child::cim:unit/@value', 'str', False),
    ]

    return set_attributes(DataTopic(), xml, nsmap, decodings)


def decode_data_property(xml, nsmap):
    """Decodes a data property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('name', 'child::cim:name/text()', 'str', False),
        ('description', 'child::cim:description/text()', 'str', False),
        ('value', 'child::cim:value/text()', 'str', False),
    ]

    return set_attributes(DataProperty(), xml, nsmap, decodings)

