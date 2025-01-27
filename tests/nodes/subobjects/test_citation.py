import json

from util import strip_uid_from_dict

import cript


def test_json(complex_citation_node, complex_citation_dict):
    c = complex_citation_node
    c_dict = strip_uid_from_dict(json.loads(c.json))
    assert c_dict == complex_citation_dict
    c2 = cript.load_nodes_from_json(c.json)
    c2_dict = strip_uid_from_dict(json.loads(c2.json))
    assert c_dict == c2_dict


def test_setter_getter(complex_citation_node, complex_reference_node):
    c = complex_citation_node
    c.type = "replicated"
    assert c.type == "replicated"
    new_ref = complex_reference_node
    new_ref.title = "foo bar"
    c.reference = new_ref
    assert c.reference == new_ref
