"""A set of xml decoding functions for the shared CIM sub-package.

"""

# Module imports.
from pycim.v1_5.types.software import *
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.core.decoding.cim_decoder_xml_for_shared_package import *


# Module exports.
__all__ = ['decode_model_component']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



def decode_model_component(xml, nsmap):
    """Decodes a model component from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', 'self::cim:modelComponent', decode_cim_info, False),
        ('types', 'child::cim:type/@value', 'str', True),
    ]

    i = decode_software_component(xml, nsmap, ModelComponent())
    return set_attributes(i, xml, nsmap, decodings)


def decode_software_component(xml, nsmap, component):
    """Decodes a software component from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('child_components', 'child::cim:childComponent/cim:modelComponent', decode_model_component, True),
        ('child_components', 'child::cim:childComponent/cim:processorComponent', decode_child_processor_component, True),
        ('citations', 'child::cim:citation', decode_citation, True),
        ('component_properties', 'child::cim:componentProperties/cim:componentProperty', decode_component_property, True),
        ('description', 'child::cim:description/text()', 'str', False),
        ('long_name', 'child::cim:longName/text()', 'str', False),
        ('release_date', 'child::cim:releaseDate/text()', 'datetime', False),
        ('responsible_parties', 'child::cim:responsibleParty', decode_responsible_party, True),
        ('short_name', 'child::cim:shortName/text()', 'str', False),
    ]
    return set_attributes(component, xml, nsmap, decodings)


def decode_component_property(xml, nsmap):
    """Decodes a component_property from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('component_properties', 'child::cim:componentProperty', decode_component_property, True),
        ('citations', 'child::cim:citation', decode_citation, True),
        ('description', 'child::cim:description/text()', 'str', False),
        ('grid'),
        ('intent', 'self::cim:componentProperty/@intent', 'str', False),
        ('is_represented', 'self::cim:componentProperty/@represented', 'bool', False),
        ('long_name', 'child::cim:longName/text()', 'str', False),
        ('short_name', 'child::cim:shortName/text()', 'str', False),
        ('standard_names', 'child::cim:standardName/@value', 'str', True),
        ('units', 'child::cim:units/@value', 'str', False),
        # TODO clarify.
        ('value', 'child::cim:value/text()', 'str', False),
        ('values'),
    ]
    return set_attributes(ComponentProperty(), xml, nsmap, decodings)


def decode_child_processor_component(xml, nsmap):
    """Decodes a child processor component from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [

    ]
    return ModelComponent()


