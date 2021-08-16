from ner_client import NamedEntityClient
from test_doubles import NERClientTestDouble

def test_get_ents_returns_dictionary():
    ner = NERClientTestDouble([])
    assert isinstance(ner.get_ents(''), dict)

def test_get_ents_maps_LOC_to_地点():
    ner = NERClientTestDouble([{'text': '地球', 'label_': 'LOC'}])
    expected_result = {'entities': [{'ent': '地球', 'label': '地点'}], 'html': ''}
    assert ner.get_ents('')['entities'] == expected_result['entities']

def test_get_ents_maps_ORDINAL_to_序数():
    ner = NERClientTestDouble([{'text': '第三', 'label_': 'ORDINAL'}])
    expected_result = {'entities': [{'ent': '第三', 'label': '序数'}], 'html': ''}
    assert ner.get_ents('')['entities'] == expected_result['entities']


def test_get_ents_maps_QUANTITY_to_基数():
    ner = NERClientTestDouble([{'text': '1公里', 'label_': 'QUANTITY'}])
    expected_result = {'entities': [{'ent': '1公里', 'label': '基数'}], 'html': ''}
    assert ner.get_ents('')['entities'] == expected_result['entities']


