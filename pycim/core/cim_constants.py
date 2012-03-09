"""Exposes set of cim constants.

"""

# Module exports.
__all__ = ['CIM_VERSIONS', 'CIM_ENCODINGS']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Set of supported CIM versions.
CIM_VERSIONS = ['1.5']


# Set of supported CIM encodings.
CIM_ENCODINGS = ['base64', 'binary', 'json', 'xml', 'yaml']

