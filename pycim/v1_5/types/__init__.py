"""A set of cim 1.5 packages.

CIM CODE GENERATOR :: Code generated @ 2012-03-20 16:28:50.001063.
"""

# Module imports.
from pycim.v1_5.types.activity.activity import Activity
from pycim.v1_5.types.activity.boundary_condition import BoundaryCondition
from pycim.v1_5.types.activity.conformance import Conformance
from pycim.v1_5.types.activity.ensemble import Ensemble
from pycim.v1_5.types.activity.ensemble_member import EnsembleMember
from pycim.v1_5.types.activity.experiment import Experiment
from pycim.v1_5.types.activity.experiment_relationship import ExperimentRelationship
from pycim.v1_5.types.activity.experiment_relationship_target import ExperimentRelationshipTarget
from pycim.v1_5.types.activity.initial_condition import InitialCondition
from pycim.v1_5.types.activity.measurement_campaign import MeasurementCampaign
from pycim.v1_5.types.activity.numerical_activity import NumericalActivity
from pycim.v1_5.types.activity.numerical_experiment import NumericalExperiment
from pycim.v1_5.types.activity.numerical_requirement import NumericalRequirement
from pycim.v1_5.types.activity.output_requirement import OutputRequirement
from pycim.v1_5.types.activity.requirement_option import RequirementOption
from pycim.v1_5.types.activity.simulation import Simulation
from pycim.v1_5.types.activity.simulation_composite import SimulationComposite
from pycim.v1_5.types.activity.simulation_relationship import SimulationRelationship
from pycim.v1_5.types.activity.simulation_relationship_target import SimulationRelationshipTarget
from pycim.v1_5.types.activity.simulation_run import SimulationRun
from pycim.v1_5.types.activity.spatio_temporal_constraint import SpatioTemporalConstraint
from pycim.v1_5.types.data.data_content import DataContent
from pycim.v1_5.types.data.data_distribution import DataDistribution
from pycim.v1_5.types.data.data_extent import DataExtent
from pycim.v1_5.types.data.data_extent_geographical import DataExtentGeographical
from pycim.v1_5.types.data.data_extent_temporal import DataExtentTemporal
from pycim.v1_5.types.data.data_extent_time_interval import DataExtentTimeInterval
from pycim.v1_5.types.data.data_hierarchy_level import DataHierarchyLevel
from pycim.v1_5.types.data.data_object import DataObject
from pycim.v1_5.types.data.data_property import DataProperty
from pycim.v1_5.types.data.data_restriction import DataRestriction
from pycim.v1_5.types.data.data_storage import DataStorage
from pycim.v1_5.types.data.data_storage_db import DataStorageDb
from pycim.v1_5.types.data.data_storage_file import DataStorageFile
from pycim.v1_5.types.data.data_storage_ip import DataStorageIp
from pycim.v1_5.types.data.data_topic import DataTopic
from pycim.v1_5.types.grids.grid_mosaic import GridMosaic
from pycim.v1_5.types.grids.grid_spec import GridSpec
from pycim.v1_5.types.shared.calendar import Calendar
from pycim.v1_5.types.shared.cim_document_relationship import CimDocumentRelationship
from pycim.v1_5.types.shared.cim_document_relationship_target import CimDocumentRelationshipTarget
from pycim.v1_5.types.shared.cim_genealogy import CimGenealogy
from pycim.v1_5.types.shared.cim_info import CimInfo
from pycim.v1_5.types.shared.cim_reference import CimReference
from pycim.v1_5.types.shared.cim_relationship import CimRelationship
from pycim.v1_5.types.shared.cim_type_info import CimTypeInfo
from pycim.v1_5.types.shared.citation import Citation
from pycim.v1_5.types.shared.closed_date_range import ClosedDateRange
from pycim.v1_5.types.shared.compiler import Compiler
from pycim.v1_5.types.shared.data_source import DataSource
from pycim.v1_5.types.shared.date_range import DateRange
from pycim.v1_5.types.shared.license import License
from pycim.v1_5.types.shared.machine import Machine
from pycim.v1_5.types.shared.machine_compiler_unit import MachineCompilerUnit
from pycim.v1_5.types.shared.open_date_range import OpenDateRange
from pycim.v1_5.types.shared.platform import Platform
from pycim.v1_5.types.shared.property import Property
from pycim.v1_5.types.shared.responsible_party import ResponsibleParty
from pycim.v1_5.types.shared.responsible_party_contact_info import ResponsiblePartyContactInfo
from pycim.v1_5.types.software.component_language import ComponentLanguage
from pycim.v1_5.types.software.component_language_property import ComponentLanguageProperty
from pycim.v1_5.types.software.component_property import ComponentProperty
from pycim.v1_5.types.software.composition import Composition
from pycim.v1_5.types.software.coupling import Coupling
from pycim.v1_5.types.software.coupling_property import CouplingProperty
from pycim.v1_5.types.software.deployment import Deployment
from pycim.v1_5.types.software.entry_point import EntryPoint
from pycim.v1_5.types.software.model_component import ModelComponent
from pycim.v1_5.types.software.parallelisation import Parallelisation
from pycim.v1_5.types.software.processor_component import ProcessorComponent
from pycim.v1_5.types.software.rank import Rank
from pycim.v1_5.types.software.software_component import SoftwareComponent
from pycim.v1_5.types.software.timing import Timing


# Module exports.
__all__ = ['Activity', 'BoundaryCondition', 'Conformance', 'Ensemble', 'EnsembleMember', 'Experiment', 'ExperimentRelationship', 'ExperimentRelationshipTarget', 'InitialCondition', 'MeasurementCampaign', 'NumericalActivity', 'NumericalExperiment', 'NumericalRequirement', 'OutputRequirement', 'RequirementOption', 'Simulation', 'SimulationComposite', 'SimulationRelationship', 'SimulationRelationshipTarget', 'SimulationRun', 'SpatioTemporalConstraint', 'DataContent', 'DataDistribution', 'DataExtent', 'DataExtentGeographical', 'DataExtentTemporal', 'DataExtentTimeInterval', 'DataHierarchyLevel', 'DataObject', 'DataProperty', 'DataRestriction', 'DataStorage', 'DataStorageDb', 'DataStorageFile', 'DataStorageIp', 'DataTopic', 'GridMosaic', 'GridSpec', 'Calendar', 'CimDocumentRelationship', 'CimDocumentRelationshipTarget', 'CimGenealogy', 'CimInfo', 'CimReference', 'CimRelationship', 'CimTypeInfo', 'Citation', 'ClosedDateRange', 'Compiler', 'DataSource', 'DateRange', 'License', 'Machine', 'MachineCompilerUnit', 'OpenDateRange', 'Platform', 'Property', 'ResponsibleParty', 'ResponsiblePartyContactInfo', 'ComponentLanguage', 'ComponentLanguageProperty', 'ComponentProperty', 'Composition', 'Coupling', 'CouplingProperty', 'Deployment', 'EntryPoint', 'ModelComponent', 'Parallelisation', 'ProcessorComponent', 'Rank', 'SoftwareComponent', 'Timing']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-20 16:28:50.001063"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"

