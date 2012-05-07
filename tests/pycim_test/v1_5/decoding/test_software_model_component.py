"""
A set of cim related unit tests.
"""

# Module imports.
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pycim.v1_5.types import *
from pycim_test.test_utils import *


# Module provenance info.
__author__="markmorgan"
__date__ ="$Aug 31, 2010 11:43:27 AM$"
__copyright__ = "Copyright 2011 - Metafor Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Target version of CIM being tested.
CIM = '1.5'

# Target type being tested.
TYPE = ModelComponent

# Test XML representation.
XML_FILE = 'software.model_component.xml'


class TestDecodeModelComponent(unittest.TestCase):
    """A decoding from xml unit test.

    """

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_open_xml(self):
        xml = get_test_xml_file(CIM, XML_FILE)
        assert xml is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(CIM, XML_FILE, TYPE)
        
        assert obj.cim_info.id == uuid.UUID('7a2b64cc-03ca-11e1-a36a-00163e9152a5')
        assert obj.cim_info.version == '1'
        assert obj.cim_info.create_date == dateutil_parser.parse('2012-01-31 12:34:51.361018')
        assert obj.cim_info.author.individual_name == 'Metafor Questionnaire'
        assert obj.cim_info.author.role == 'documentAuthor'
        assert len(obj.cim_info.genealogy.relationships) == 1
        r = obj.cim_info.genealogy.relationships[0]
        assert r.description.startswith('The HadGEM2-A model')
        assert r.direction == 'toTarget'
        assert r.target.reference.name == 'HadGEM1'
        assert r.type == 'previousVersionOf'

        print obj.activity
        assert obj.activity is None
        assert obj.timing is None
        assert len(obj.types ) == 1
        t = obj.types[0]
        assert t == 'model'
        assert len(obj.child_components) == 4
        cc = obj.child_components[0]
        assert len(cc.child_components) == 3
        assert len(cc.component_properties) == 4
        assert len(cc.responsible_parties) == 4
        assert cc.short_name == 'Aerosols'
        assert len(cc.types) == 2
        assert cc.cim_info.id == uuid.UUID('7a44cb24-03ca-11e1-a36a-00163e9152a5')
        cp = cc.component_properties[0]
        assert len(cp.component_properties) == 6
        assert cp.intent == 'interactive'
        assert cp.is_represented == True
        assert cp.long_name == 'Aerosols'
        assert cp.short_name == 'Aerosol Key Properties'
        assert cp.value == None
        cp = cp.component_properties[0]
        assert len(cp.component_properties) == 0
        assert cp.intent == None
        assert cp.is_represented == True
        assert cp.long_name == 'AerosolSchemeScope'
        assert cp.short_name == 'AerosolSchemeScope'
        assert cp.value == 'whole atmosphere'
        cp = cc.component_properties[1]
        assert cp.description.startswith('Emissions of aerosols')
        assert cp.units == 'kg/m2/s'
        assert len(cp.standard_names) == 2
        sn = cp.standard_names[0]
        assert sn == 'biomass_burning_carbon_flux'
        sn = cp.standard_names[1]
        assert sn == 'carbon_flux'
        assert len(obj.citations) == 2
        c = obj.citations[0]
        assert c.collective_title.startswith('Bellouin')
        assert c.location.startswith("http://www.metoffice.gov.uk/publications/HCTN/HCTN_73.pdf")
        assert c.title.startswith('Bellouin')
        c = obj.citations[1]
        assert c.collective_title.startswith('Collins')
        assert c.location.startswith("http://www.metoffice.gov.uk/publications/HCTN/HCTN_74.pdf")
        assert c.title.startswith('Collins')
        assert obj.component_language is None
        assert obj.component_properties == []
        assert obj.composition is None
        assert obj.coupling_framework is None
        assert obj.dependencies == []
        assert obj.deployments == []
        assert obj.description.startswith('The HadGEM2-A model')
        assert obj.funding_sources == []
        assert obj.grid is None
        assert obj.is_embedded == False
        assert obj.license is None
        assert obj.long_name == 'Hadley Global Environment Model 2 - Atmosphere'
        assert obj.numerical_properties == []
        # TODO default for uri's = None ?
        assert obj.online_resource == str()
        assert obj.parent_component is None
        # TODO default for str's = None ?
        assert obj.previous_version == str()
        assert obj.release_date == dateutil_parser.parse('2009')
        assert len(obj.responsible_parties) == 4
        rp = obj.responsible_parties[0]
        assert rp.abbreviation == 'Chris Jones'
        assert rp.contact_info.address.startswith('Met Office Hadley Centre')
        assert rp.contact_info.email is None
        assert rp.contact_info.url.startswith('http://www.metoffice.gov.uk/research/our-scientists/climate-chemistry-ecosystems/chris-jones')
        assert rp.individual_name == 'Chris Jones'
        assert rp.role == 'PI'
        rp = obj.responsible_parties[2]
        assert rp.abbreviation == 'Gill Martin'
        assert rp.contact_info.address.startswith('Met Office Hadley Centre')
        assert rp.contact_info.email == 'mark.webb@metoffice.gov.uk'
        assert rp.contact_info.url.startswith('http://www.metoffice.gov.uk/research/people/gill-martin')
        assert rp.individual_name == 'Gill Martin'
        assert rp.role == 'contact'
        assert obj.scientific_properties == []
        assert obj.short_name == 'HadGEM2-A'


    def test_representation_dict(self):
        d = decode_dict_from_xml(CIM, XML_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True
        
        assert d['cim_info']['id'] == uuid.UUID('7a2b64cc-03ca-11e1-a36a-00163e9152a5')

        assert d['short_name'] == 'HadGEM2-A'
        assert len(d['types']) == 1
        assert len(d['child_components']) == 4
        cc = d['child_components'][0]
        assert len(cc['child_components']) == 3
        assert cc['short_name'] == 'Aerosols'
        assert cc['cim_info']['id'] == uuid.UUID('7a44cb24-03ca-11e1-a36a-00163e9152a5')
        cp = cc['component_properties'][0]
        assert len(cp['component_properties']) == 6
        assert cp['intent'] == 'interactive'
        assert cp['short_name'] == 'Aerosol Key Properties'


    def test_representation_json(self):
        do_test_from_xml_file(CIM, XML_FILE, 'json')


    def test_representation_base64(self):
        do_test_from_xml_file(CIM, XML_FILE, 'base64')





