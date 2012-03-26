"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-26 18:08:48.698826.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.decoding.decoder_for_shared_package import *
from pycim.v1_5.types.grids import *


# Module exports.
__all__ = [
    "decode_grid_mosaic", 
    "decode_grid_spec"
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-26 18:08:48.698826"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_grid_mosaic(xml, nsmap):
    """Decodes a grid mosaic instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
    ]

    return set_attributes(GridMosaic(), xml, nsmap, decodings)


def decode_grid_spec(xml, nsmap):
    """Decodes a grid spec instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:dataObject'),
        ('esm_exchange_grids', True, decode_grid_mosaic, 'child::cim:esmExchangeGrid'),
        ('esm_model_grids', True, decode_grid_mosaic, 'child::cim:esmModelGrid'),
    ]

    return set_attributes(GridSpec(), xml, nsmap, decodings)


