"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-28 15:02:44.726394.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

# Intra/Inter-package imports.
from pycim.v1_5.types.shared.citation import Citation
from pycim.v1_5.types.grids.grid_extent import GridExtent
from pycim.v1_5.types.grids.grid_tile import GridTile



# Module exports.
__all__ = ['GridMosaic']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-28 15:02:44.726394$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class GridMosaic(object):
    """A class within the cim v1.5 type system.

    The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.
    """
    def __init__(self):
        """Constructor"""
        super(GridMosaic, self).__init__()

        self.__citations = []                                       # type = shared.Citation
        self.__description = str()                                  # type = str
        self.__extent = None                                        # type = grids.GridExtent
        self.__has_congruent_tiles = bool()                         # type = bool
        self.__id = str()                                           # type = str
        self.__is_leaf = bool()                                     # type = bool
        self.__long_name = str()                                    # type = str
        self.__mnemonic = str()                                     # type = str
        self.__mosaic_count = int()                                 # type = int
        self.__mosaics = []                                         # type = grids.GridMosaic
        self.__short_name = str()                                   # type = str
        self.__tile_count = int()                                   # type = int
        self.__tiles = []                                           # type = grids.GridTile
        self.__type = str()                                         # type = str


    @property
    def citations(self):
        """Gets value of {class-name} citations property.

        Optional container element for specifying a list of references that describe the grid."""
        return list(self.__citations)

    @citations.setter
    def citations(self, value):
        """Sets value of {class-name} citations property.

        Optional container element for specifying a list of references that describe the grid."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__citations = []
        for i in value:
            self.append_to_citations(i)

    @citations.deleter
    def citations(self, value):
        """Deletes {class-name} citations property."""
        raise TypeError("Cannot delete {class-name} citations property.")

    def append_to_citations(self, item):
        """Appends an item to the managed {class-name} citations collection."""
        if not isinstance(item, Citation):
            raise TypeError("item is of incorrect type.")
        self.__citations.append(item)

    def remove_from_citations(self, item):
        """Removes an item from the managed {class-name} citations collection."""
        if not isinstance(item, Citation):
            raise TypeError("item is of incorrect type.")
        self.__citations.remove(item)


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of a grid mosaic."""
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
    def has_congruent_tiles(self):
        """Gets value of {class-name} has_congruent_tiles property.

        Indicates whether or not all the tiles contained within a grid mosaic are congruent, that is, of the same size and shape."""
        return self.__has_congruent_tiles

    @has_congruent_tiles.setter
    def has_congruent_tiles(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} has_congruent_tiles property."""
        self.__has_congruent_tiles = value

    @has_congruent_tiles.deleter
    def has_congruent_tiles(self, value):
        """Deletes {class-name} has_congruent_tiles property."""
        raise TypeError("Cannot delete {class-name} has_congruent_tiles property.")


    @property
    def id(self):
        """Gets value of grid mosaic id property.

        Specifies a globally unique identifier for a grid mosaic instance. By globally we mean across all GridSpec instances/records within a given modelling activity (such as CMIP5)."""
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid mosaic id property."""
        self.__id = value

    @id.deleter
    def id(self, value):
        """Deletes grid mosaic id property."""
        raise TypeError("Cannot delete grid mosaic id property.")


    @property
    def is_leaf(self):
        """Gets value of grid mosaic is_leaf property.

        Indicates whether or not a grid mosaic is a leaf mosaic, that is, it only contains child grid tiles not further mosaics."""
        return self.__is_leaf

    @is_leaf.setter
    def is_leaf(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, bool):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid mosaic is_leaf property."""
        self.__is_leaf = value

    @is_leaf.deleter
    def is_leaf(self, value):
        """Deletes grid mosaic is_leaf property."""
        raise TypeError("Cannot delete grid mosaic is_leaf property.")


    @property
    def long_name(self):
        """Gets value of {class-name} long_name property.

        Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes."""
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
    def mosaic_count(self):
        """Gets value of {class-name} mosaic_count property.

        Specifies the number of mosaics associated with a non-leaf grid mosaic. Set to zero if the grid mosaic is a leaf mosaic, i.e. it contains child grid tiles not mosaics."""
        return self.__mosaic_count

    @mosaic_count.setter
    def mosaic_count(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} mosaic_count property."""
        self.__mosaic_count = value

    @mosaic_count.deleter
    def mosaic_count(self, value):
        """Deletes {class-name} mosaic_count property."""
        raise TypeError("Cannot delete {class-name} mosaic_count property.")


    @property
    def mosaics(self):
        """Gets value of {class-name} mosaics property."""
        return list(self.__mosaics)

    @mosaics.setter
    def mosaics(self, value):
        """Sets value of {class-name} mosaics property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__mosaics = []
        for i in value:
            self.append_to_mosaics(i)

    @mosaics.deleter
    def mosaics(self, value):
        """Deletes {class-name} mosaics property."""
        raise TypeError("Cannot delete {class-name} mosaics property.")

    def append_to_mosaics(self, item):
        """Appends an item to the managed {class-name} mosaics collection."""
        if not isinstance(item, GridMosaic):
            raise TypeError("item is of incorrect type.")
        self.__mosaics.append(item)

    def remove_from_mosaics(self, item):
        """Removes an item from the managed {class-name} mosaics collection."""
        if not isinstance(item, GridMosaic):
            raise TypeError("item is of incorrect type.")
        self.__mosaics.remove(item)


    @property
    def short_name(self):
        """Gets value of grid mosaic short_name property.

        Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. 'UM ATM N96'."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid mosaic short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes grid mosaic short_name property."""
        raise TypeError("Cannot delete grid mosaic short_name property.")


    @property
    def tile_count(self):
        """Gets value of {class-name} tile_count property.

        Specifies the number of tiles associated with a leaf grid mosaic. Set to zero if the grid mosaic is not a leaf mosaic, i.e. it contains child grid mosaics rather than tiles. (Added to align with equivalent ESG/Curator property.)"""
        return self.__tile_count

    @tile_count.setter
    def tile_count(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} tile_count property."""
        self.__tile_count = value

    @tile_count.deleter
    def tile_count(self, value):
        """Deletes {class-name} tile_count property."""
        raise TypeError("Cannot delete {class-name} tile_count property.")


    @property
    def tiles(self):
        """Gets value of {class-name} tiles property."""
        return list(self.__tiles)

    @tiles.setter
    def tiles(self, value):
        """Sets value of {class-name} tiles property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__tiles = []
        for i in value:
            self.append_to_tiles(i)

    @tiles.deleter
    def tiles(self, value):
        """Deletes {class-name} tiles property."""
        raise TypeError("Cannot delete {class-name} tiles property.")

    def append_to_tiles(self, item):
        """Appends an item to the managed {class-name} tiles collection."""
        if not isinstance(item, GridTile):
            raise TypeError("item is of incorrect type.")
        self.__tiles.append(item)

    def remove_from_tiles(self, item):
        """Removes an item from the managed {class-name} tiles collection."""
        if not isinstance(item, GridTile):
            raise TypeError("item is of incorrect type.")
        self.__tiles.remove(item)


    @property
    def type(self):
        """Gets value of grid mosaic type property.

        Specifies the type of all the grid tiles contained in a grid mosaic. It is assumed that all of the tiles comprising a given grid mosaic are of the same type. The value domain is as per the specified enumeration list."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of grid mosaic type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes grid mosaic type property."""
        raise TypeError("Cannot delete grid mosaic type property.")



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
        append(d, 'citations', self.__citations, True, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'extent', self.__extent, False, False, False)
        append(d, 'has_congruent_tiles', self.__has_congruent_tiles, False, True, False)
        append(d, 'id', self.__id, False, True, False)
        append(d, 'is_leaf', self.__is_leaf, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'mnemonic', self.__mnemonic, False, True, False)
        append(d, 'mosaic_count', self.__mosaic_count, False, True, False)
        append(d, 'mosaics', self.__mosaics, True, False, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        append(d, 'tile_count', self.__tile_count, False, True, False)
        append(d, 'tiles', self.__tiles, True, False, False)
        append(d, 'type', self.__type, False, True, False)
        return d





# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm.



# Command line entry point.
if __name__ == "__main__":
    try:
        i = GridMosaic()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('grids.GridMosaic', e)
