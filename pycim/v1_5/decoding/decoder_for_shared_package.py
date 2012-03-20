"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-20 16:28:49.993741.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.types.shared import *


# Module exports.
__all__ = [
    "decode_calendar", 
    "decode_cim_document_relationship", 
    "decode_cim_document_relationship_target", 
    "decode_cim_genealogy", 
    "decode_cim_info", 
    "decode_cim_reference", 
    "decode_cim_relationship", 
    "decode_cim_type_info", 
    "decode_citation", 
    "decode_closed_date_range", 
    "decode_compiler", 
    "decode_data_source", 
    "decode_date_range", 
    "decode_license", 
    "decode_machine", 
    "decode_machine_compiler_unit", 
    "decode_open_date_range", 
    "decode_platform", 
    "decode_property", 
    "decode_responsible_party", 
    "decode_responsible_party_contact_info"
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-20 16:28:49.993741"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_calendar(xml, nsmap):
    """Decodes a calendar instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Calendar(), xml, nsmap, decodings)


def decode_cim_document_relationship(xml, nsmap):
    """Decodes a cim document relationship instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('target', False, decode_cim_document_relationship_target, 'child::cim:target'),
        ('type', False, 'str', 'self::cim:documentRelationship/@type'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('direction', False, 'str', 'self::cim:documentRelationship/@direction'),
    ]

    return set_attributes(CimDocumentRelationship(), xml, nsmap, decodings)


def decode_cim_document_relationship_target(xml, nsmap):
    """Decodes a cim document relationship target instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('reference', False, decode_cim_reference, 'child::cim:reference'),
    ]

    return set_attributes(CimDocumentRelationshipTarget(), xml, nsmap, decodings)


def decode_cim_genealogy(xml, nsmap):
    """Decodes a cim genealogy instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('relationships', True, decode_cim_document_relationship, 'child::cim:relationship/cim:documentRelationship'),
    ]

    return set_attributes(CimGenealogy(), xml, nsmap, decodings)


def decode_cim_info(xml, nsmap):
    """Decodes a cim info instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('author', False, decode_responsible_party, 'child::cim:documentAuthor'),
        ('create_date', False, 'datetime', 'child::cim:documentCreationDate/text()'),
        ('genealogy', False, decode_cim_genealogy, 'child::cim:documentGenealogy'),
        ('id', False, 'uuid', 'child::cim:documentID/text()'),
        ('version', False, 'str', 'child::cim:documentVersion/text()'),
    ]

    return set_attributes(CimInfo(), xml, nsmap, decodings)


def decode_cim_reference(xml, nsmap):
    """Decodes a cim reference instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('external_id', False, 'str', 'child::cim:externalID/text()'),
        ('id', False, 'uuid', 'child::cim:id/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('type', False, 'str', 'child::cim:type/text()'),
        ('version', False, 'str', 'child::cim:version/text()'),
    ]

    return set_attributes(CimReference(), xml, nsmap, decodings)


def decode_cim_relationship(xml, nsmap):
    """Decodes a cim relationship instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(CimRelationship(), xml, nsmap, decodings)


def decode_cim_type_info(xml, nsmap):
    """Decodes a cim type info instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(CimTypeInfo(), xml, nsmap, decodings)


def decode_citation(xml, nsmap):
    """Decodes a citation instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('alternative_title', False, 'str', 'child::gmd:alternateTitle/gco:CharacterString/text()'),
        ('collective_title', False, 'str', 'gmd:collectiveTitle/gco:CharacterString/text()'),
        ('date', False, 'datetime', 'child::gmd:date/gmd:CI_Date/gmd:date/gco:Date/text()'),
        ('date_type', False, 'str', 'child::gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue'),
        ('location', False, 'str', 'child::gmd:otherCitationDetails/gco:CharacterString/text()'),
        ('title', False, 'str', 'child::gmd:title/gco:CharacterString/text()'),
        ('type', False, 'str', 'child::gmd:presentationForm/gmd:CI_PresentationFormCode/@codeListValue'),
    ]

    return set_attributes(Citation(), xml, nsmap, decodings)


def decode_closed_date_range(xml, nsmap):
    """Decodes a closed date range instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('end', False, 'datetime', 'child::cim:endDate/text()'),
        ('start', False, 'datetime', 'child::cim:startDate/text()'),
        ('duration', False, 'str', 'child::cim:duration/text()'),
    ]

    return set_attributes(ClosedDateRange(), xml, nsmap, decodings)


def decode_compiler(xml, nsmap):
    """Decodes a compiler instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Compiler(), xml, nsmap, decodings)


def decode_data_source(xml, nsmap):
    """Decodes a data source instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(DataSource(), xml, nsmap, decodings)


def decode_date_range(xml, nsmap):
    """Decodes a date range instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('duration', False, 'str', 'child::cim:duration/text()'),
    ]

    return set_attributes(DateRange(), xml, nsmap, decodings)


def decode_license(xml, nsmap):
    """Decodes a license instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(License(), xml, nsmap, decodings)


def decode_machine(xml, nsmap):
    """Decodes a machine instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Machine(), xml, nsmap, decodings)


def decode_machine_compiler_unit(xml, nsmap):
    """Decodes a machine compiler unit instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(MachineCompilerUnit(), xml, nsmap, decodings)


def decode_open_date_range(xml, nsmap):
    """Decodes a open date range instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('end', False, 'datetime', 'child::cim:endDate/text()'),
        ('start', False, 'datetime', 'child::cim:startDate/text()'),
        ('duration', False, 'str', 'child::cim:duration/text()'),
    ]

    return set_attributes(OpenDateRange(), xml, nsmap, decodings)


def decode_platform(xml, nsmap):
    """Decodes a platform instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:platform'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
    ]

    return set_attributes(Platform(), xml, nsmap, decodings)


def decode_property(xml, nsmap):
    """Decodes a property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name/text()'),
        ('value', False, 'str', 'child::cim:value/text()'),
    ]

    return set_attributes(Property(), xml, nsmap, decodings)


def decode_responsible_party(xml, nsmap):
    """Decodes a responsible party instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('abbreviation', False, 'str', 'child::cim:abbreviation/text()'),
        ('contact_info', False, decode_responsible_party_contact_info, 'child::gmd:contactInfo/gmd:CI_Contact'),
        ('individual_name', False, 'str', 'child::gmd:individualName/gco:CharacterString/text()'),
        ('organisation_name', False, 'str', 'child::gmd:organisationName/gco:CharacterString/text()'),
        ('role', False, 'str', 'gmd:role/gmd:CI_RoleCode/@codeListValue'),
    ]

    return set_attributes(ResponsibleParty(), xml, nsmap, decodings)


def decode_responsible_party_contact_info(xml, nsmap):
    """Decodes a responsible party contact info instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('address', False, 'str', 'child::gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString/text()'),
        ('email', False, 'str', 'child::gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString/text()'),
        ('url', False, 'str', 'child::gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()'),
    ]

    return set_attributes(ResponsiblePartyContactInfo(), xml, nsmap, decodings)


