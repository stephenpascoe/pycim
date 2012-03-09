"""A set of xml decoding functions for the shared CIM sub-package.

"""

# Module imports.
from pycim.v1_5.types.shared import *
from pycim.core.decoding.cim_decoder_xml_utils import *

# Module exports.
__all__ = ['decode_cim_info',
           'decode_citation',
           'decode_responsible_party',
           'decode_property']

           
# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



def decode_cim_info(xml, nsmap):
    """Returns set of cim info related decodings.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ['author', 'child::cim:documentAuthor', decode_responsible_party, False],
        ['create_date', 'child::cim:documentCreationDate/text()', 'datetime', False],
        ['id', 'child::cim:documentID/text()', 'uuid', False],
        ['version', 'child::cim:documentVersion/text()', 'str', False],
        ['genealogy', 'child::cim:documentGenealogy', decode_cim_geneaology, False],
    ]

    return set_attributes(CimInfo(), xml, nsmap, decodings)


def decode_cim_document_relationship(xml, nsmap):
    """Decodes a document_relationship from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', 'child::cim:description/text()', 'str', False),
        ('direction', 'self::cim:documentRelationship/@direction', 'str', False),
        ('type', 'self::cim:documentRelationship/@type', 'str', False),
        ('target', 'child::cim:target', decode_cim_document_relationship_target, False),
    ]

    return set_attributes(CimDocumentRelationship(), xml, nsmap, decodings)


def decode_cim_document_relationship_target(xml, nsmap):
    """Decodes a document_relationship_target from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('reference', 'child::cim:reference', decode_cim_reference, False),
    ]
    return set_attributes(CimDocumentRelationshipTarget(), xml, nsmap, decodings)


def decode_cim_geneaology(xml, nsmap):
    """Decodes a geneaology from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('relationships', 'child::cim:relationship/cim:documentRelationship', decode_cim_document_relationship, True),
    ]

    return set_attributes(CimGenealogy(), xml, nsmap, decodings)


def decode_cim_reference(xml, nsmap):
    """Decodes a reference from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    from lxml import etree as et
    print et.tostring(xml)

    decodings = [
        ('id', 'child::cim:id/text()', 'uid', False),
        ('name', 'child::cim:name/text()', 'str', False),
        ('type', 'child::cim:type/text()', 'str', False),
        ('version', 'child::cim:version/text()', 'str', False),
        ('external_id', 'child::cim:externalID/text()', 'str', False),
        ('description', 'child::cim:description/text()', 'str', False),
    ]

    return set_attributes(CimReference(), xml, nsmap, decodings)


def decode_citation(xml, nsmap):
    """Decodes a citation from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('alternative_title', 'child::gmd:alternateTitle/gco:CharacterString/text()', 'str', False),
        ('collective_title', 'gmd:collectiveTitle/gco:CharacterString/text()', 'str', False),
        ('date', 'child::gmd:date/gmd:CI_Date/gmd:date/gco:Date/text()', 'datetime', False),
        ('date_type', 'child::gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue', 'str', False),
        ('location', 'child::gmd:otherCitationDetails/gco:CharacterString/text()', 'str', False),
        ('title', 'child::gmd:title/gco:CharacterString/text()', 'str', False),
        ('type', 'child::gmd:presentationForm/gmd:CI_PresentationFormCode/@codeListValue', 'str', False),
    ]

    return set_attributes(Citation(), xml, nsmap, decodings)


def decode_property(xml, nsmap):
    """Decodes a property from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('name', 'child::cim:name/text()', 'str', False),
        ('value', 'child::cim:value/text()', 'str', False),
    ]

    return set_attributes(Property(), xml, nsmap, decodings)


def decode_responsible_party(xml, nsmap):
    """Decodes a responsible party from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('abbreviation', 'child::cim:abbreviation/text()', 'str', False),
        ('contact_info', 'child::gmd:contactInfo/gmd:CI_Contact', decode_responsible_party_contact_info, False),
        ('individual_name', 'child::gmd:individualName/gco:CharacterString/text()', 'str', False),
        ('organisation_name', 'child::gmd:organisationName/gco:CharacterString/text()', 'str', False),
        ('role', 'gmd:role/gmd:CI_RoleCode/@codeListValue', 'str', False),
    ]

    return set_attributes(ResponsibleParty(), xml, nsmap, decodings)


def decode_responsible_party_contact_info(xml, nsmap):
    """Decodes a responsible party contact info from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('address', 'child::gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString/text()', 'str', False),
        ('email', 'child::gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString/text()', 'str', False),
        ('url', 'child::gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()', 'str', False),
    ]

    return set_attributes(ResponsiblePartyContactInfo(), xml, nsmap, decodings)