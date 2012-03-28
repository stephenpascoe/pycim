"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 16:29:10.558697.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.decoding.decoder_for_shared_package import *
from pycim.v1_5.types.grids import *


# Module exports.
__all__ = [
    "decode_coordinate_list", 
    "decode_grid_extent", 
    "decode_grid_mosaic", 
    "decode_grid_property", 
    "decode_grid_spec", 
    "decode_grid_tile", 
    "decode_grid_tile_resolution_type", 
    "decode_vertical_coordinate_list"
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-28 16:29:10.558697"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_coordinate_list(xml, nsmap):
    """Decodes a coordinate list instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('length', False, 'int', '@length'),
        ('uom', False, 'str', '@uom'),
    ]

    return set_attributes(CoordinateList(), xml, nsmap, decodings)


def decode_grid_extent(xml, nsmap):
    """Decodes a grid extent instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('maximum_latitude', False, 'int', 'child::cim:latMax/text()'),
        ('maximum_longitude', False, 'int', 'child::cim:lonMax/text()'),
        ('minimum_latitude', False, 'int', 'child::cim:latMin/text()'),
        ('minimum_longitude', False, 'int', 'child::cim:lonMin/text()'),
        ('units', False, 'str', 'child::cim:units/text()'),
    ]

    return set_attributes(GridExtent(), xml, nsmap, decodings)


def decode_grid_mosaic(xml, nsmap):
    """Decodes a grid mosaic instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('citations', True, decode_citation, 'child::cim:citationList/cim:citation'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('has_congruent_tiles', False, 'bool', '@congruentTiles'),
        ('id', False, 'str', '@id'),
        ('is_leaf', False, 'bool', '@isLeaf'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('mnemonic', False, 'str', 'child::cim:mnemonic/text()'),
        ('mosaic_count', False, 'int', '@numMosaics'),
        ('mosaics', True, decode_grid_mosaic, 'child::cim:gridMosaic'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('tile_count', False, 'int', '@numTiles'),
        ('tiles', True, decode_grid_tile, 'child::cim:gridTile'),
        ('type', False, 'str', '@gridType'),
    ]

    return set_attributes(GridMosaic(), xml, nsmap, decodings)


def decode_grid_property(xml, nsmap):
    """Decodes a grid property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name/text()'),
        ('value', False, 'str', 'child::cim:value/text()'),
    ]

    return set_attributes(GridProperty(), xml, nsmap, decodings)


def decode_grid_spec(xml, nsmap):
    """Decodes a grid spec instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:gridSpec'),
        ('esm_exchange_grids', True, decode_grid_mosaic, 'child::cim:esmExchangeGrid'),
        ('esm_model_grids', True, decode_grid_mosaic, 'child::cim:esmModelGrid'),
    ]

    return set_attributes(GridSpec(), xml, nsmap, decodings)


def decode_grid_tile(xml, nsmap):
    """Decodes a grid tile instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('discretization_type', False, 'str', '@discretizationType'),
        ('extent', False, decode_grid_extent, 'child::cim:extent'),
        ('geometry_type', False, 'str', '@geometryType'),
        ('horizontal_resolution', False, decode_grid_tile_resolution_type, 'child::cim:horizontalResolution'),
        ('id', False, 'str', '@id'),
        ('is_conformal', False, 'bool', '@isConformal'),
        ('is_regular', False, 'bool', '@isRegular'),
        ('is_terrain_following', False, 'bool', '@isTerrainFollowing'),
        ('is_uniform', False, 'bool', '@isUniform'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('mnemonic', False, 'str', 'child::cim:mnemonic/text()'),
        ('nx', False, 'int', '@nx'),
        ('ny', False, 'int', '@ny'),
        ('nz', False, 'int', '@nz'),
        ('refinement_scheme', False, 'str', '@refinementScheme'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('vertical_resolution', False, decode_grid_tile_resolution_type, 'child::cim:verticalResolution'),
        ('zcoords', False, decode_vertical_coordinate_list, 'child::cim:zcoords'),
    ]

    return set_attributes(GridTile(), xml, nsmap, decodings)


def decode_grid_tile_resolution_type(xml, nsmap):
    """Decodes a grid tile resolution type instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', '@description'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
    ]

    return set_attributes(GridTileResolutionType(), xml, nsmap, decodings)


def decode_vertical_coordinate_list(xml, nsmap):
    """Decodes a vertical coordinate list instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('form', False, 'str', '@coordinateForm'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
        ('type', False, 'str', '@coordinateType'),
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('length', False, 'int', '@length'),
        ('uom', False, 'str', '@uom'),
    ]

    return set_attributes(VerticalCoordinateList(), xml, nsmap, decodings)


