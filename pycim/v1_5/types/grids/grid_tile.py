"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-05-02 12:24:01.250272.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.grids.discretization_enum import DiscretizationEnum
from pycim.v1_5.types.grids.grid_extent import GridExtent
from pycim.v1_5.types.grids.geometry_type_enum import GeometryTypeEnum
from pycim.v1_5.types.grids.grid_tile_resolution_type import GridTileResolutionType
from pycim.v1_5.types.grids.refinement_type_enum import RefinementTypeEnum
from pycim.v1_5.types.grids.vertical_coordinate_list import VerticalCoordinateList



# Module exports.
__all__ = ['GridTile']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-05-02 12:24:01.250272$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridTile(object):
    """A class within the cim v1.5 type system.

    The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.
    """
    def __init__(self):
        """Constructor"""
        super(GridTile, self).__init__()

        self.__area = str()                                         # type = str
        self.__cell_array = str()                                   # type = str
        self.__cell_ref_array = str()                               # type = str
        self.__coord_file = str()                                   # type = str
        self.__coordinate_pole = str()                              # type = str
        self.__description = str()                                  # type = str
        self.__discretization_type = None                           # type = grids.DiscretizationEnum
        self.__extent = None                                        # type = grids.GridExtent
        self.__geometry_type = None                                 # type = grids.GeometryTypeEnum
        self.__grid_north_pole = str()                              # type = str
        self.__horizontal_crs = str()                               # type = str
        self.__horizontal_resolution = None                         # type = grids.GridTileResolutionType
        self.__id = str()                                           # type = str
        self.__is_conformal = bool()                                # type = bool
        self.__is_regular = bool()                                  # type = bool
        self.__is_terrain_following = bool()                        # type = bool
        self.__is_uniform = bool()                                  # type = bool
        self.__long_name = str()                                    # type = str
        self.__mnemonic = str()                                     # type = str
        self.__nx = int()                                           # type = int
        self.__ny = int()                                           # type = int
        self.__nz = int()                                           # type = int
        self.__refinement_scheme = None                             # type = grids.RefinementTypeEnum
        self.__short_name = str()                                   # type = str
        self.__simple_grid_geom = str()                             # type = str
        self.__vertical_crs = str()                                 # type = str
        self.__vertical_resolution = None                           # type = grids.GridTileResolutionType
        self.__zcoords = None                                       # type = grids.VerticalCoordinateList


    @property
    def area(self):
        """Gets value of {class-name} area property.

        gml:MeasureType:Specifies the area of the grid tile in the units defined by the uom attribute that is attached to the GML MeasureType data type."""
        return self.__area

    @area.setter
    def area(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} area property."""
        self.__area = value

    @area.deleter
    def area(self, value):
        """Deletes {class-name} area property."""
        raise TypeError("Cannot delete {class-name} area property.")


    @property
    def cell_array(self):
        """Gets value of {class-name} cell_array property.

        GridCellArray:This property may be used to specify an array of grid cell definitions which together define the coordinate geometry of a grid tile. Depending on context, any of the existing sub-types of GridCell may be used. Mixing types is, however, not currently permitted."""
        return self.__cell_array

    @cell_array.setter
    def cell_array(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} cell_array property."""
        self.__cell_array = value

    @cell_array.deleter
    def cell_array(self, value):
        """Deletes {class-name} cell_array property."""
        raise TypeError("Cannot delete {class-name} cell_array property.")


    @property
    def cell_ref_array(self):
        """Gets value of {class-name} cell_ref_array property.

        GridCellArray:This property may be used to define the coordinate geometry of a grid tile by specifying an array of references to remotely defined grid cells. Depending on context, any of the existing sub-types of GridCell may be referenced."""
        return self.__cell_ref_array

    @cell_ref_array.setter
    def cell_ref_array(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} cell_ref_array property."""
        self.__cell_ref_array = value

    @cell_ref_array.deleter
    def cell_ref_array(self, value):
        """Deletes {class-name} cell_ref_array property."""
        raise TypeError("Cannot delete {class-name} cell_ref_array property.")


    @property
    def coord_file(self):
        """Gets value of {class-name} coord_file property.

        This property may be used to specify the URI of a file containing grid coordinates that define the geometry of a a grid tile. It is envisaged that this will be the preferred mechanism for specifying the geometry of complex grids."""
        return self.__coord_file

    @coord_file.setter
    def coord_file(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} coord_file property."""
        self.__coord_file = value

    @coord_file.deleter
    def coord_file(self, value):
        """Deletes {class-name} coord_file property."""
        raise TypeError("Cannot delete {class-name} coord_file property.")


    @property
    def coordinate_pole(self):
        """Gets value of {class-name} coordinate_pole property.

        gml:PointType:The coordinatePole property may be used to specify the lat-long position of any coordinate poles (in the mathematical sense) that form part of the definition of a grid tile. Not to be confused with the gridNorthPole property.  If required, two or more coordinate pole definitions may be distinguished by setting the gml:id attribute to appropriate values, such as spole, npole, etc."""
        return self.__coordinate_pole

    @coordinate_pole.setter
    def coordinate_pole(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} coordinate_pole property."""
        self.__coordinate_pole = value

    @coordinate_pole.deleter
    def coordinate_pole(self, value):
        """Deletes {class-name} coordinate_pole property."""
        raise TypeError("Cannot delete {class-name} coordinate_pole property.")


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of a grid tile."""
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} description property."""
        self.__description = value

    @description.deleter
    def description(self, value):
        """Deletes {class-name} description property."""
        raise TypeError("Cannot delete {class-name} description property.")


    @property
    def discretization_type(self):
        """Gets value of {class-name} discretization_type property.

        Indicates the type of discretization applied to the grid tile, e.g. "logically_rectangular"."""
        return self.__discretization_type

    @discretization_type.setter
    def discretization_type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} discretization_type property."""
        self.__discretization_type = value

    @discretization_type.deleter
    def discretization_type(self, value):
        """Deletes {class-name} discretization_type property."""
        raise TypeError("Cannot delete {class-name} discretization_type property.")


    @property
    def extent(self):
        """Gets value of {class-name} extent property."""
        return self.__extent

    @extent.setter
    def extent(self, value):
        if value is not None and not isinstance(value, GridExtent):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} extent property."""
        self.__extent = value

    @extent.deleter
    def extent(self, value):
        """Deletes {class-name} extent property."""
        raise TypeError("Cannot delete {class-name} extent property.")


    @property
    def geometry_type(self):
        """Gets value of {class-name} geometry_type property.

        Indicates the geometric figure used to approximate the figure of the Earth, e.g. "sphere"."""
        return self.__geometry_type

    @geometry_type.setter
    def geometry_type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} geometry_type property."""
        self.__geometry_type = value

    @geometry_type.deleter
    def geometry_type(self, value):
        """Deletes {class-name} geometry_type property."""
        raise TypeError("Cannot delete {class-name} geometry_type property.")


    @property
    def grid_north_pole(self):
        """Gets value of {class-name} grid_north_pole property.

        gml:PointType:If required, defines the lat-long position of the north pole used by the grid tile in the case of rotated/displaced pole grids. Not to be confused with the coordinatePole property."""
        return self.__grid_north_pole

    @grid_north_pole.setter
    def grid_north_pole(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} grid_north_pole property."""
        self.__grid_north_pole = value

    @grid_north_pole.deleter
    def grid_north_pole(self, value):
        """Deletes {class-name} grid_north_pole property."""
        raise TypeError("Cannot delete {class-name} grid_north_pole property.")


    @property
    def horizontal_crs(self):
        """Gets value of {class-name} horizontal_crs property.

        gml:CRSPropertyType:Specifies the horizontal coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external horizontal CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document."""
        return self.__horizontal_crs

    @horizontal_crs.setter
    def horizontal_crs(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} horizontal_crs property."""
        self.__horizontal_crs = value

    @horizontal_crs.deleter
    def horizontal_crs(self, value):
        """Deletes {class-name} horizontal_crs property."""
        raise TypeError("Cannot delete {class-name} horizontal_crs property.")


    @property
    def horizontal_resolution(self):
        """Gets value of {class-name} horizontal_resolution property.

        Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch)."""
        return self.__horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, value):
        if value is not None and not isinstance(value, GridTileResolutionType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} horizontal_resolution property."""
        self.__horizontal_resolution = value

    @horizontal_resolution.deleter
    def horizontal_resolution(self, value):
        """Deletes {class-name} horizontal_resolution property."""
        raise TypeError("Cannot delete {class-name} horizontal_resolution property.")


    @property
    def id(self):
        """Gets value of {class-name} id property.

        Specifies an identifer for a grid tile that is unique within its parent grid mosaic. It is not required for this identifier to be unique either across all mosaics in a GridSpec or across all GridSpecs, though if that were the case it would not be detrimental."""
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} id property."""
        self.__id = value

    @id.deleter
    def id(self, value):
        """Deletes {class-name} id property."""
        raise TypeError("Cannot delete {class-name} id property.")


    @property
    def is_conformal(self):
        """Gets value of {class-name} is_conformal property.

        This property is used to indicate if the grid tile is conformal, i.e. angle-preserving. If so, angles measured on the grid are equal to the equivalent angles on the Earth."""
        return self.__is_conformal

    @is_conformal.setter
    def is_conformal(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_conformal property."""
        self.__is_conformal = value

    @is_conformal.deleter
    def is_conformal(self, value):
        """Deletes {class-name} is_conformal property."""
        raise TypeError("Cannot delete {class-name} is_conformal property.")


    @property
    def is_regular(self):
        """Gets value of {class-name} is_regular property.

        If true, indicates that the horizontal coordinates of the grid can be defined using 1D arrays (vectors). This means that grid node locations are defined by the cartesian product of the X/Lon and Y/Lat coordinate vectors. It also means that grid cells are logically rectangular (they may also be physically rectangular in the case of projected coordinates)."""
        return self.__is_regular

    @is_regular.setter
    def is_regular(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_regular property."""
        self.__is_regular = value

    @is_regular.deleter
    def is_regular(self, value):
        """Deletes {class-name} is_regular property."""
        raise TypeError("Cannot delete {class-name} is_regular property.")


    @property
    def is_terrain_following(self):
        """Gets value of {class-name} is_terrain_following property.

        Set to true if the vertical coordinate system is terrain-following even if, as is often the case, this only applies to the lower levels of the grid."""
        return self.__is_terrain_following

    @is_terrain_following.setter
    def is_terrain_following(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_terrain_following property."""
        self.__is_terrain_following = value

    @is_terrain_following.deleter
    def is_terrain_following(self, value):
        """Deletes {class-name} is_terrain_following property."""
        raise TypeError("Cannot delete {class-name} is_terrain_following property.")


    @property
    def is_uniform(self):
        """Gets value of {class-name} is_uniform property.

        If true, indicates that horizontal coordinates have fixed offsets in the X and Y directions. If the offset is the same in both directions then the grids are logically square, otherwise they are logically rectangular. The offsets can be specified by two scalar values (or three values in the case of 3D grids)."""
        return self.__is_uniform

    @is_uniform.setter
    def is_uniform(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_uniform property."""
        self.__is_uniform = value

    @is_uniform.deleter
    def is_uniform(self, value):
        """Deletes {class-name} is_uniform property."""
        raise TypeError("Cannot delete {class-name} is_uniform property.")


    @property
    def long_name(self):
        """Gets value of {class-name} long_name property."""
        return self.__long_name

    @long_name.setter
    def long_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} long_name property."""
        self.__long_name = value

    @long_name.deleter
    def long_name(self, value):
        """Deletes {class-name} long_name property."""
        raise TypeError("Cannot delete {class-name} long_name property.")


    @property
    def mnemonic(self):
        """Gets value of {class-name} mnemonic property."""
        return self.__mnemonic

    @mnemonic.setter
    def mnemonic(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} mnemonic property."""
        self.__mnemonic = value

    @mnemonic.deleter
    def mnemonic(self, value):
        """Deletes {class-name} mnemonic property."""
        raise TypeError("Cannot delete {class-name} mnemonic property.")


    @property
    def nx(self):
        """Gets value of {class-name} nx property.

        Specifies the length of the X, or longitude, dimension of the grid tile."""
        return self.__nx

    @nx.setter
    def nx(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} nx property."""
        self.__nx = value

    @nx.deleter
    def nx(self, value):
        """Deletes {class-name} nx property."""
        raise TypeError("Cannot delete {class-name} nx property.")


    @property
    def ny(self):
        """Gets value of {class-name} ny property.

        Specifies the length of the Y, or latitude, dimension of the grid tile."""
        return self.__ny

    @ny.setter
    def ny(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} ny property."""
        self.__ny = value

    @ny.deleter
    def ny(self, value):
        """Deletes {class-name} ny property."""
        raise TypeError("Cannot delete {class-name} ny property.")


    @property
    def nz(self):
        """Gets value of {class-name} nz property.

        Specifies the length of the Z, or height/level, dimension of the grid tile. The zcoords coordinate list property, if specified, should have this length."""
        return self.__nz

    @nz.setter
    def nz(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} nz property."""
        self.__nz = value

    @nz.deleter
    def nz(self, value):
        """Deletes {class-name} nz property."""
        raise TypeError("Cannot delete {class-name} nz property.")


    @property
    def refinement_scheme(self):
        """Gets value of {class-name} refinement_scheme property."""
        return self.__refinement_scheme

    @refinement_scheme.setter
    def refinement_scheme(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} refinement_scheme property."""
        self.__refinement_scheme = value

    @refinement_scheme.deleter
    def refinement_scheme(self, value):
        """Deletes {class-name} refinement_scheme property."""
        raise TypeError("Cannot delete {class-name} refinement_scheme property.")


    @property
    def short_name(self):
        """Gets value of {class-name} short_name property."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes {class-name} short_name property."""
        raise TypeError("Cannot delete {class-name} short_name property.")


    @property
    def simple_grid_geom(self):
        """Gets value of {class-name} simple_grid_geom property.

        SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type."""
        return self.__simple_grid_geom

    @simple_grid_geom.setter
    def simple_grid_geom(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} simple_grid_geom property."""
        self.__simple_grid_geom = value

    @simple_grid_geom.deleter
    def simple_grid_geom(self, value):
        """Deletes {class-name} simple_grid_geom property."""
        raise TypeError("Cannot delete {class-name} simple_grid_geom property.")


    @property
    def vertical_crs(self):
        """Gets value of {class-name} vertical_crs property.

        gml:CRSPropertyType:Specifies the vertical coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external vertical CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document."""
        return self.__vertical_crs

    @vertical_crs.setter
    def vertical_crs(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} vertical_crs property."""
        self.__vertical_crs = value

    @vertical_crs.deleter
    def vertical_crs(self, value):
        """Deletes {class-name} vertical_crs property."""
        raise TypeError("Cannot delete {class-name} vertical_crs property.")


    @property
    def vertical_resolution(self):
        """Gets value of {class-name} vertical_resolution property.

        Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property)."""
        return self.__vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, value):
        if value is not None and not isinstance(value, GridTileResolutionType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} vertical_resolution property."""
        self.__vertical_resolution = value

    @vertical_resolution.deleter
    def vertical_resolution(self, value):
        """Deletes {class-name} vertical_resolution property."""
        raise TypeError("Cannot delete {class-name} vertical_resolution property.")


    @property
    def zcoords(self):
        """Gets value of {class-name} zcoords property.

        This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods."""
        return self.__zcoords

    @zcoords.setter
    def zcoords(self, value):
        if value is not None and not isinstance(value, VerticalCoordinateList):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} zcoords property."""
        self.__zcoords = value

    @zcoords.deleter
    def zcoords(self, value):
        """Deletes {class-name} zcoords property."""
        raise TypeError("Cannot delete {class-name} zcoords property.")



    def as_dict(self):
        """Gets dictionary representation of self used to create other representations such as json, xml ...etc.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'area', self.__area, False, True, False)
        append(d, 'cell_array', self.__cell_array, False, True, False)
        append(d, 'cell_ref_array', self.__cell_ref_array, False, True, False)
        append(d, 'coord_file', self.__coord_file, False, True, False)
        append(d, 'coordinate_pole', self.__coordinate_pole, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'discretization_type', self.__discretization_type, False, False, True)
        append(d, 'extent', self.__extent, False, False, False)
        append(d, 'geometry_type', self.__geometry_type, False, False, True)
        append(d, 'grid_north_pole', self.__grid_north_pole, False, True, False)
        append(d, 'horizontal_crs', self.__horizontal_crs, False, True, False)
        append(d, 'horizontal_resolution', self.__horizontal_resolution, False, False, False)
        append(d, 'id', self.__id, False, True, False)
        append(d, 'is_conformal', self.__is_conformal, False, True, False)
        append(d, 'is_regular', self.__is_regular, False, True, False)
        append(d, 'is_terrain_following', self.__is_terrain_following, False, True, False)
        append(d, 'is_uniform', self.__is_uniform, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'mnemonic', self.__mnemonic, False, True, False)
        append(d, 'nx', self.__nx, False, True, False)
        append(d, 'ny', self.__ny, False, True, False)
        append(d, 'nz', self.__nz, False, True, False)
        append(d, 'refinement_scheme', self.__refinement_scheme, False, False, True)
        append(d, 'short_name', self.__short_name, False, True, False)
        append(d, 'simple_grid_geom', self.__simple_grid_geom, False, True, False)
        append(d, 'vertical_crs', self.__vertical_crs, False, True, False)
        append(d, 'vertical_resolution', self.__vertical_resolution, False, False, False)
        append(d, 'zcoords', self.__zcoords, False, False, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridTile()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridTile', e)
