"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-02-15 15:48:21.204070.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.decoding.decoder_for_shared_package import decode_cim_reference
from pycim.v1_5.decoding.decoder_for_shared_package import decode_cim_reference
from pycim.v1_5.types.activity.experiment_relationship import ExperimentRelationship
from pycim.v1_5.types.activity.experiment_relationship_target import ExperimentRelationshipTarget
from pycim.v1_5.types.activity.numerical_experiment import NumericalExperiment
from pycim.v1_5.types.activity.simulation_relationship import SimulationRelationship
from pycim.v1_5.types.activity.simulation_relationship_target import SimulationRelationshipTarget


# Module exports.
__all__ = [
    'decode_experiment_relationship', 
    'decode_experiment_relationship_target', 
    'decode_numerical_experiment', 
    'decode_simulation_relationship', 
    'decode_simulation_relationship_target'
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-02-15 15:48:21.204070"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_experiment_relationship(xml, nsmap):
    """Decodes a experiment relationship instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(ExperimentRelationship(), xml, nsmap, decodings)


def decode_experiment_relationship_target(xml, nsmap):
    """Decodes a experiment relationship target instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(ExperimentRelationshipTarget(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes a numerical experiment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(NumericalExperiment(), xml, nsmap, decodings)


def decode_simulation_relationship(xml, nsmap):
    """Decodes a simulation relationship instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(SimulationRelationship(), xml, nsmap, decodings)


def decode_simulation_relationship_target(xml, nsmap):
    """Decodes a simulation relationship target instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(SimulationRelationshipTarget(), xml, nsmap, decodings)


