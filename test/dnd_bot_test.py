import pytest
import json
from dnd_bot import Dnd_Bot

def test_exists():
    assert Dnd_Bot

def test_instantiate():
    assert Dnd_Bot()

def test_requests(url_setup):
    fact1 = Dnd_Bot()
    fact1.url = url_setup
    fact1.fact_request()
    assert fact1.fact
    
def test_request_url(url_setup):
    fact1 = Dnd_Bot()
    fact1.url = url_setup
    assert fact1.url is not None

def test_request_url_return(url_setup, url_request_return ):
    fact1 = Dnd_Bot()
    fact1.url = url_setup
    fact1.fact_request()
    assert fact1.fact == url_request_return
    
def test_json_data_url(url_part):
    fact1 = Dnd_Bot()
    fact1.import_url_from_json()
    assert fact1.data['results'][0]['url'] == '/api/alignments/chaotic-evil'
    
@pytest.fixture
def url_setup():
     url = "https://www.dnd5eapi.co/api/ability-scores/str"
     return url
 
@pytest.fixture
def url_request_return():
    strength_return = {'index': 'str', 'name': 'STR', 'full_name': 'Strength', 'desc': ['Strength measures bodily power, athletic training, and the extent to which you can exert raw physical force.', 'A Strength check can model any attempt to lift, push, pull, or break something, to force your body through a space, or to otherwise apply brute force to a situation. The Athletics skill reflects aptitude in certain kinds of Strength checks.'], 'skills': [{'name': 'Athletics', 'index': 'athletics', 'url': '/api/skills/athletics'}], 'url': '/api/ability-scores/str'}
    return strength_return

@pytest.fixture
def url_part():
    with open('url_builder_data.json') as f:
        data = json.load(f)
    return data
