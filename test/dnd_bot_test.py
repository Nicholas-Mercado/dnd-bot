import pytest
from dnd_bot import Dnd_Bot

def test_exists():
    assert Dnd_Bot

def test_instantiate():
    assert Dnd_Bot()

def test_requests():
    fact1 =Dnd_Bot()
    fact1.fact_request()
    assert fact1.fact
    
