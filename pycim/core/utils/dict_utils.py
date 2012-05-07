"""Set of dictionary utilitiy functions

"""
# Module imports.


# Module exports.
__all__ = ['convert_dict_keys']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


def convert_dict_keys(d, key_formatter):
    """
    Converts keys of a dictionary using the passed key formatter.

    Keyword Arguments:
    d - a dictionary to be converted.
    key_formatter - a dictionary key formatting function pointer.

    """
    r = {}
    for key, value in d.items():
        if isinstance(value, dict):
            r[key_formatter(key)] = convert_dict_keys(value, key_formatter)
        else:
            r[key_formatter(key)] = value
    return r

