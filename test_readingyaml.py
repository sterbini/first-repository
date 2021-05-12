import readingyaml as ry
import numpy as np
import pytest
import yaml
import datetime
import ruamel

def test_exeption():
    with pytest.raises(Exception):
        ry.readyaml()


with open('hamishtest.yml', 'r') as f:
    yaml = ruamel.yaml.YAML()
    test_data = yaml.load(f)


def test_valid_number():
    assert test_data == ordereddict([('first', ordereddict([('hr', datetime.datetime(2021, 5, 11, 16, 50, 39, 84511)), ('unix', 1620751839.08453), ('mycomment', 'hello')]))])

def test_append():
    ry.append_yaml({'blue': 'bonjour'}, ('hamishtest.yml'))
    assert ry.read_yaml('hamishtest.yml') == ordereddict([('first', ordereddict([('hr', datetime.datetime(2021, 5, 11, 16, 50, 39, 84511)), ('unix', 1620751839.08453), ('mycomment', 'hello')])), ('blue', 'bonjour')])

