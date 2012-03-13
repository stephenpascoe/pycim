"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-13 14:59:06.824753.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.decoding.decoder_for_shared_package import *
from pycim.v1_5.types.activity import *


# Module exports.
__all__ = [
    "decode_activity", 
    "decode_boundary_condition", 
    "decode_experiment", 
    "decode_experiment_relationship", 
    "decode_experiment_relationship_target", 
    "decode_initial_condition", 
    "decode_measurement_campaign", 
    "decode_numerical_experiment", 
    "decode_numerical_requirement", 
    "decode_output_requirement", 
    "decode_requirement_option", 
    "decode_simulation_relationship", 
    "decode_simulation_relationship_target", 
    "decode_spatio_temporal_constraint"
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-13 14:59:06.824753"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_activity(xml, nsmap):
    """Decodes a activity instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
    ]

    return set_attributes(Activity(), xml, nsmap, decodings)


def decode_boundary_condition(xml, nsmap):
    """Decodes a boundary condition instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('id', False, 'str', 'child::cim:id/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('options', True, decode_requirement_option, 'child::cim:requirementOption'),
    ]

    return set_attributes(BoundaryCondition(), xml, nsmap, decodings)


def decode_experiment(xml, nsmap):
    """Decodes a experiment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
    ]

    return set_attributes(Experiment(), xml, nsmap, decodings)


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


def decode_initial_condition(xml, nsmap):
    """Decodes a initial condition instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('id', False, 'str', 'child::cim:id/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('options', True, decode_requirement_option, 'child::cim:requirementOption'),
    ]

    return set_attributes(InitialCondition(), xml, nsmap, decodings)


def decode_measurement_campaign(xml, nsmap):
    """Decodes a measurement campaign instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
    ]

    return set_attributes(MeasurementCampaign(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes a numerical experiment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:numericalExperiment'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('experiment_id', False, 'str', 'child::cim:experimentID/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement/cim:boundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement/cim:outputRequirement'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
    ]

    return set_attributes(NumericalExperiment(), xml, nsmap, decodings)


def decode_numerical_requirement(xml, nsmap):
    """Decodes a numerical requirement instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('id', False, 'str', 'child::cim:id/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('options', True, decode_requirement_option, 'child::cim:requirementOption'),
    ]

    return set_attributes(NumericalRequirement(), xml, nsmap, decodings)


def decode_output_requirement(xml, nsmap):
    """Decodes a output requirement instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('id', False, 'str', 'child::cim:id/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('options', True, decode_requirement_option, 'child::cim:requirementOption'),
    ]

    return set_attributes(OutputRequirement(), xml, nsmap, decodings)


def decode_requirement_option(xml, nsmap):
    """Decodes a requirement option instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('relationship', False, 'str', 'self::cim:requirementOption/@optionRelationship'),
        ('requirement', False, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirement', False, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirement', False, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirement', False, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
    ]

    return set_attributes(RequirementOption(), xml, nsmap, decodings)


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


def decode_spatio_temporal_constraint(xml, nsmap):
    """Decodes a spatio temporal constraint instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('date_range', False, decode_closed_date_range, 'child::cim:requiredDuration/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:requiredDuration/cim:openDateRange'),
        ('spatial_resolution', False, 'str', 'child::cim:spatialResolution/text()'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('id', False, 'str', 'child::cim:id/text()'),
        ('name', False, 'str', 'child::cim:name/text()'),
        ('options', True, decode_requirement_option, 'child::cim:requirementOption'),
    ]

    return set_attributes(SpatioTemporalConstraint(), xml, nsmap, decodings)


