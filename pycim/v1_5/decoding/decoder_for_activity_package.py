"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-26 18:08:48.690167.
"""

# Module imports.
from pycim.core.decoding.cim_decoder_xml_utils import *
from pycim.v1_5.decoding.decoder_for_data_package import *
from pycim.v1_5.decoding.decoder_for_shared_package import *
from pycim.v1_5.decoding.decoder_for_software_package import *
from pycim.v1_5.types.activity import *


# Module exports.
__all__ = [
    "decode_activity", 
    "decode_boundary_condition", 
    "decode_conformance", 
    "decode_ensemble", 
    "decode_ensemble_member", 
    "decode_experiment", 
    "decode_experiment_relationship", 
    "decode_experiment_relationship_target", 
    "decode_initial_condition", 
    "decode_measurement_campaign", 
    "decode_numerical_activity", 
    "decode_numerical_experiment", 
    "decode_numerical_requirement", 
    "decode_output_requirement", 
    "decode_physical_modification", 
    "decode_requirement_option", 
    "decode_simulation", 
    "decode_simulation_composite", 
    "decode_simulation_relationship", 
    "decode_simulation_relationship_target", 
    "decode_simulation_run", 
    "decode_spatio_temporal_constraint"
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-26 18:08:48.690167"
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
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
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


def decode_conformance(xml, nsmap):
    """Decodes a conformance instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('is_conformant', False, 'bool', 'self::@conformant'),
        ('requirement_references', True, decode_cim_reference, 'child::cim:requirement/cim:reference'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('source_references', True, decode_cim_reference, 'child::cim:source/cim:reference'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('type', False, 'str', 'self::@type'),
    ]

    return set_attributes(Conformance(), xml, nsmap, decodings)


def decode_ensemble(xml, nsmap):
    """Decodes a ensemble instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:ensemble'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(Ensemble(), xml, nsmap, decodings)


def decode_ensemble_member(xml, nsmap):
    """Decodes a ensemble member instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(EnsembleMember(), xml, nsmap, decodings)


def decode_experiment(xml, nsmap):
    """Decodes a experiment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
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
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(MeasurementCampaign(), xml, nsmap, decodings)


def decode_numerical_activity(xml, nsmap):
    """Decodes a numerical activity instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(NumericalActivity(), xml, nsmap, decodings)


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
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
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


def decode_physical_modification(xml, nsmap):
    """Decodes a physical modification instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('is_conformant', False, 'bool', 'self::@conformant'),
        ('requirement_references', True, decode_cim_reference, 'child::cim:requirement/cim:reference'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('source_references', True, decode_cim_reference, 'child::cim:source/cim:reference'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('type', False, 'str', 'self::@type'),
    ]

    return set_attributes(PhysicalModification(), xml, nsmap, decodings)


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


def decode_simulation(xml, nsmap):
    """Decodes a simulation instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('authors', False, 'str', 'child::cim:authorsList/cim:list/text()'),
        ('conformances', True, decode_conformance, 'child::cim:authorsList/cim:list/text()'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('simulation_id', False, 'str', 'child::cim:simulationID/text()'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(Simulation(), xml, nsmap, decodings)


def decode_simulation_composite(xml, nsmap):
    """Decodes a simulation composite instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('child', True, decode_simulation_run, 'child::cim:child'),
        ('child', True, decode_simulation_composite, 'child::cim:child'),
        ('cim_info', False, decode_cim_info, 'self::cim:simulationRun'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('rank', False, 'int', 'child::cim:rank/text()'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list/text()'),
        ('conformances', True, decode_conformance, 'child::cim:authorsList/cim:list/text()'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('simulation_id', False, 'str', 'child::cim:simulationID/text()'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(SimulationComposite(), xml, nsmap, decodings)


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


def decode_simulation_run(xml, nsmap):
    """Decodes a simulation run instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:simulationRun'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('model', False, decode_model_component, 'child::cim:model/cim:modelComponent'),
        ('model_reference', False, decode_cim_reference, 'child::cim:model/cim:reference'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list/text()'),
        ('conformances', True, decode_conformance, 'child::cim:authorsList/cim:list/text()'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('simulation_id', False, 'str', 'child::cim:simulationID/text()'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource/text()'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(SimulationRun(), xml, nsmap, decodings)


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


